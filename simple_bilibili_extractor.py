#!/usr/bin/env python3
"""
Simple Bilibili Subtitle Extractor
Script đơn giản để tách subtitle từ Bilibili sử dụng yt-dlp trực tiếp
"""

import subprocess
import json
import sys
import os
from pathlib import Path

def extract_bilibili_subtitles(url, output_dir="subtitles"):
    """
    Tách subtitle từ video Bilibili
    
    Args:
        url (str): URL video Bilibili
        output_dir (str): Thư mục lưu subtitle
    
    Returns:
        dict: Thông tin về subtitle đã tách
    """
    print(f"🎯 Đang tách subtitle từ: {url}")
    
    # Tạo thư mục output nếu chưa tồn tại
    Path(output_dir).mkdir(exist_ok=True)
    
    # Command yt-dlp để tải subtitle
    cmd = [
        "yt-dlp",
        "--write-subs",           # Tải subtitle
        "--write-auto-subs",      # Tải auto-generated subtitle
        "--sub-langs", "zh-CN,zh-TW,en,ja,ko,all",  # Ngôn ngữ subtitle
        "--sub-format", "srt/ass/vtt/best",         # Format subtitle
        "--skip-download",        # Chỉ tải subtitle, không tải video
        "--output", f"{output_dir}/%(title)s.%(ext)s",
        url
    ]
    
    try:
        print("📥 Đang tải subtitle...")
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        print("✅ Tải subtitle thành công!")
        print(f"📁 Subtitle được lưu trong thư mục: {output_dir}")
        
        # Liệt kê các file subtitle đã tải
        subtitle_files = []
        for file_path in Path(output_dir).glob("*"):
            if file_path.suffix in ['.srt', '.ass', '.vtt']:
                subtitle_files.append(str(file_path))
                print(f"   📄 {file_path.name}")
        
        return {
            "success": True,
            "subtitle_files": subtitle_files,
            "output_dir": output_dir,
            "message": f"Đã tải {len(subtitle_files)} file subtitle"
        }
        
    except subprocess.CalledProcessError as e:
        error_msg = f"Lỗi khi tải subtitle: {e.stderr}"
        print(f"❌ {error_msg}")
        return {
            "success": False,
            "error": error_msg,
            "stderr": e.stderr,
            "stdout": e.stdout
        }
    except FileNotFoundError:
        error_msg = "yt-dlp không được tìm thấy. Vui lòng cài đặt yt-dlp: pip install yt-dlp"
        print(f"❌ {error_msg}")
        return {
            "success": False,
            "error": error_msg
        }

def get_video_info(url):
    """
    Lấy thông tin video từ Bilibili
    
    Args:
        url (str): URL video Bilibili
    
    Returns:
        dict: Thông tin video
    """
    print(f"📋 Đang lấy thông tin video: {url}")
    
    cmd = [
        "yt-dlp",
        "--dump-json",
        "--no-download",
        url
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        video_info = json.loads(result.stdout)
        
        info = {
            "title": video_info.get("title", "Unknown"),
            "uploader": video_info.get("uploader", "Unknown"),
            "duration": video_info.get("duration", 0),
            "view_count": video_info.get("view_count", 0),
            "upload_date": video_info.get("upload_date", "Unknown"),
            "description": video_info.get("description", "")[:200] + "..." if video_info.get("description", "") else "",
            "available_subtitles": list(video_info.get("subtitles", {}).keys()),
            "automatic_captions": list(video_info.get("automatic_captions", {}).keys())
        }
        
        print(f"📺 Tiêu đề: {info['title']}")
        print(f"👤 Uploader: {info['uploader']}")
        print(f"⏱️  Thời lượng: {info['duration']} giây")
        print(f"👁️  Lượt xem: {info['view_count']:,}")
        print(f"🗣️  Subtitle có sẵn: {', '.join(info['available_subtitles']) or 'Không có'}")
        print(f"🤖 Auto captions: {', '.join(info['automatic_captions']) or 'Không có'}")
        
        return {
            "success": True,
            "info": info
        }
        
    except subprocess.CalledProcessError as e:
        error_msg = f"Lỗi khi lấy thông tin video: {e.stderr}"
        print(f"❌ {error_msg}")
        return {
            "success": False,
            "error": error_msg
        }
    except json.JSONDecodeError as e:
        error_msg = f"Lỗi parse JSON: {str(e)}"
        print(f"❌ {error_msg}")
        return {
            "success": False,
            "error": error_msg
        }

def main():
    """Hàm main"""
    print("🚀 Simple Bilibili Subtitle Extractor")
    print("=" * 50)
    
    if len(sys.argv) < 2:
        print("❌ Cách sử dụng:")
        print(f"   python3 {sys.argv[0]} <URL_BILIBILI>")
        print()
        print("📝 Ví dụ:")
        print(f"   python3 {sys.argv[0]} https://www.bilibili.com/video/BV1xx411c7mu")
        print(f"   python3 {sys.argv[0]} https://b23.tv/abc123")
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Kiểm tra URL Bilibili
    if not ("bilibili.com" in url or "b23.tv" in url):
        print("⚠️  Cảnh báo: URL này có thể không phải từ Bilibili")
    
    # Lấy thông tin video trước
    print("\n🔍 Bước 1: Lấy thông tin video")
    info_result = get_video_info(url)
    
    if not info_result["success"]:
        print("❌ Không thể lấy thông tin video. Thoát.")
        sys.exit(1)
    
    # Tách subtitle
    print("\n📥 Bước 2: Tách subtitle")
    extract_result = extract_bilibili_subtitles(url)
    
    if extract_result["success"]:
        print(f"\n🎉 Hoàn thành! {extract_result['message']}")
        print(f"📁 Kiểm tra thư mục: {extract_result['output_dir']}")
    else:
        print(f"\n❌ Thất bại: {extract_result['error']}")
        sys.exit(1)

if __name__ == "__main__":
    main()