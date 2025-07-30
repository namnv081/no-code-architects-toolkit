from flask import Blueprint
from app_utils import *
import logging
import os
import yt_dlp
import tempfile
from werkzeug.utils import secure_filename
import uuid
from services.cloud_storage import upload_file
from services.authentication import authenticate
from services.file_management import download_file
from urllib.parse import quote, urlparse
import requests

v1_media_bilibili_subtitle_bp = Blueprint('v1_media_bilibili_subtitle', __name__)
logger = logging.getLogger(__name__)

@v1_media_bilibili_subtitle_bp.route('/v1/media/bilibili/subtitle', methods=['POST'])
@authenticate
@validate_payload({
    "type": "object",
    "properties": {
        "video_url": {"type": "string", "format": "uri", "description": "URL của video Bilibili"},
        "languages": {
            "type": "array", 
            "items": {"type": "string"},
            "description": "Danh sách ngôn ngữ subtitle cần tải (vd: ['zh-Hans', 'en', 'vi'])"
        },
        "format": {
            "type": "string",
            "enum": ["srt", "vtt", "json3"],
            "default": "srt",
            "description": "Định dạng subtitle"
        },
        "cloud_upload": {
            "type": "boolean",
            "default": True,
            "description": "Có upload lên cloud storage không"
        },
        "cookie": {
            "type": "string",
            "description": "Cookie để truy cập video private (nếu cần)"
        }
    },
    "required": ["video_url"],
    "additionalProperties": False
})
@queue_task_wrapper(bypass_queue=False)
def download_bilibili_subtitle(job_id, data):
    video_url = data['video_url']
    languages = data.get('languages', [])
    subtitle_format = data.get('format', 'srt')
    cloud_upload = data.get('cloud_upload', True)
    cookie = data.get('cookie')

    logger.info(f"Job {job_id}: Received Bilibili subtitle download request for {video_url}")

    try:
        # Create a temporary directory for downloads
        with tempfile.TemporaryDirectory() as temp_dir:
            # Configure yt-dlp options for Bilibili
            ydl_opts = {
                'format': 'best',  # Download best quality
                'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s'),
                'quiet': True,
                'no_warnings': True,
                'download': False,  # Don't download video, just extract info
                'writesubtitles': True,
                'writeallsubtitles': not languages,  # Download all if no specific languages
                'subtitlesformat': subtitle_format,
                'extractor_args': {
                    'bilibili': {
                        'cookie': cookie if cookie else None
                    }
                }
            }

            # Add specific languages if provided
            if languages:
                ydl_opts['subtitleslangs'] = languages

            # Add cookies if provided
            if cookie:
                if os.path.isfile(cookie):
                    ydl_opts['cookiefile'] = cookie
                elif urlparse(cookie).scheme in ('http', 'https'):
                    # If cookie is a URL, download it first
                    ydl_opts['cookiefile'] = download_file(cookie, temp_dir)
                else:
                    # If cookie is a string, write it to a temporary file
                    cookie_file = os.path.join(temp_dir, 'cookies.txt')
                    with open(cookie_file, 'w') as f:
                        f.write(cookie)
                    ydl_opts['cookiefile'] = cookie_file

            # Extract video info and subtitles
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(video_url, download=False)
                
                # Prepare response
                response = {
                    "video_info": {
                        "title": info.get('title'),
                        "uploader": info.get('uploader'),
                        "duration": info.get('duration'),
                        "view_count": info.get('view_count'),
                        "upload_date": info.get('upload_date'),
                        "description": info.get('description')
                    },
                    "subtitles": {}
                }

                # Process subtitles if available
                if 'subtitles' in info:
                    logger.info(f"Job {job_id}: Found subtitles in info: {info['subtitles']}")
                    
                    # If no languages specified, use all available languages
                    if not languages:
                        languages = list(info['subtitles'].keys())
                        logger.info(f"Job {job_id}: No languages specified, using all available: {languages}")
                    
                    for lang, subtitle_list in info['subtitles'].items():
                        # Skip if language not in requested list
                        if lang not in languages:
                            continue
                            
                        try:
                            logger.info(f"Job {job_id}: Processing subtitle for language {lang}")
                            # Find the requested format
                            subtitle_data = None
                            for subtitle in subtitle_list:
                                if subtitle['ext'] == subtitle_format:
                                    subtitle_data = subtitle
                                    break
                                    
                            if not subtitle_data:
                                logger.warning(f"Job {job_id}: Requested format {subtitle_format} not available for {lang}")
                                continue
                            
                            # If cloud upload is requested, download and upload the subtitle
                            if cloud_upload:
                                try:
                                    subtitle_path = download_file(subtitle_data['url'], temp_dir)
                                    cloud_url = upload_file(subtitle_path)
                                    subtitle_data['url'] = cloud_url
                                    subtitle_data['cloud_url'] = cloud_url
                                except Exception as e:
                                    logger.warning(f"Job {job_id}: Failed to download subtitle for {lang}: {str(e)}")
                                    continue
                            
                            # Add subtitle data to response using language code as key
                            response["subtitles"][lang] = subtitle_data
                            logger.info(f"Job {job_id}: Successfully processed subtitle for {lang}")
                        except Exception as e:
                            logger.error(f"Job {job_id}: Error processing subtitle: {str(e)}")
                            continue
                else:
                    logger.info(f"Job {job_id}: No subtitles found for this video")
                    response["message"] = "Không tìm thấy subtitle cho video này"
                
                return response, "/v1/media/bilibili/subtitle", 200

    except Exception as e:
        logger.error(f"Job {job_id}: Error during Bilibili subtitle download process - {str(e)}")
        return str(e), "/v1/media/bilibili/subtitle", 500