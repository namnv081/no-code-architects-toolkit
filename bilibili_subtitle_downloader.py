#!/usr/bin/env python3
"""
Bilibili Subtitle Downloader
Tải subtitle từ video Bilibili sử dụng API có sẵn
"""

import requests
import json
import sys
import os
import argparse
from urllib.parse import urlparse
from typing import Dict, List, Optional

class BilibiliSubtitleDownloader:
    def __init__(self, api_url: str, api_key: str):
        """
        Khởi tạo downloader
        
        Args:
            api_url: URL của API server
            api_key: API key để xác thực
        """
        self.api_url = api_url.rstrip('/')
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    
    def download_subtitle(self, 
                         video_url: str, 
                         languages: Optional[List[str]] = None,
                         format: str = "srt",
                         cloud_upload: bool = True,
                         cookie: Optional[str] = None) -> Dict:
        """
        Tải subtitle từ video Bilibili
        
        Args:
            video_url: URL của video Bilibili
            languages: Danh sách ngôn ngữ (vd: ["zh-Hans", "en"])
            format: Định dạng subtitle (srt, vtt, json3, xml)
            cloud_upload: Có upload lên cloud storage không
            cookie: Cookie cho video private
            
        Returns:
            Dict chứa thông tin subtitle đã tải
        """
        
        # Chuẩn bị request data
        data = {
            "media_url": video_url,
            "subtitles": {
                "download": True,
                "format": format
            },
            "cloud_upload": cloud_upload
        }
        
        # Thêm languages nếu được chỉ định
        if languages:
            data["subtitles"]["languages"] = languages
        
        # Thêm cookie nếu được cung cấp
        if cookie:
            data["cookie"] = cookie
        
        try:
            print(f"🔄 Đang tải subtitle từ: {video_url}")
            print(f"📋 Tham số: {json.dumps(data, indent=2, ensure_ascii=False)}")
            
            # Gọi API
            response = requests.post(
                f"{self.api_url}/v1/BETA/media/download",
                headers=self.headers,
                json=data,
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                print("✅ Tải subtitle thành công!")
                return result
            else:
                print(f"❌ Lỗi API: {response.status_code}")
                print(f"Thông báo: {response.text}")
                return {"error": response.text}
                
        except requests.exceptions.ConnectionError:
            print("❌ Lỗi kết nối: Kiểm tra lại URL API và kết nối mạng")
            return {"error": "Connection error"}
        except requests.exceptions.Timeout:
            print("❌ Timeout: Request mất quá nhiều thời gian")
            return {"error": "Timeout"}
        except Exception as e:
            print(f"❌ Lỗi không xác định: {str(e)}")
            return {"error": str(e)}
    
    def save_subtitle_to_file(self, result: Dict, output_dir: str = ".") -> List[str]:
        """
        Lưu subtitle vào file local
        
        Args:
            result: Kết quả từ API
            output_dir: Thư mục output
            
        Returns:
            List các file đã lưu
        """
        saved_files = []
        
        if "subtitles" not in result:
            print("❌ Không có subtitle trong kết quả")
            return saved_files
        
        # Tạo thư mục output nếu chưa có
        os.makedirs(output_dir, exist_ok=True)
        
        video_title = result.get("media", {}).get("title", "unknown")
        # Làm sạch tên file
        safe_title = "".join(c for c in video_title if c.isalnum() or c in (' ', '-', '_')).rstrip()
        
        for lang, subtitle_info in result["subtitles"].items():
            try:
                # Tải file subtitle
                subtitle_url = subtitle_info.get("url")
                if not subtitle_url:
                    print(f"⚠️ Không có URL cho subtitle {lang}")
                    continue
                
                print(f"📥 Đang tải subtitle {lang}...")
                subtitle_response = requests.get(subtitle_url, timeout=30)
                
                if subtitle_response.status_code == 200:
                    # Tạo tên file
                    ext = subtitle_info.get("ext", "txt")
                    filename = f"{safe_title}_{lang}.{ext}"
                    filepath = os.path.join(output_dir, filename)
                    
                    # Lưu file
                    with open(filepath, 'wb') as f:
                        f.write(subtitle_response.content)
                    
                    print(f"✅ Đã lưu: {filepath}")
                    saved_files.append(filepath)
                else:
                    print(f"❌ Không thể tải subtitle {lang}: {subtitle_response.status_code}")
                    
            except Exception as e:
                print(f"❌ Lỗi khi lưu subtitle {lang}: {str(e)}")
        
        return saved_files
    
    def print_result_summary(self, result: Dict):
        """In tóm tắt kết quả"""
        
        if "error" in result:
            print(f"❌ Lỗi: {result['error']}")
            return
        
        print("\n" + "="*50)
        print("📊 TÓM TẮT KẾT QUẢ")
        print("="*50)
        
        # Thông tin video
        media_info = result.get("media", {})
        print(f"🎬 Video: {media_info.get('title', 'N/A')}")
        print(f"👤 Uploader: {media_info.get('uploader', 'N/A')}")
        print(f"⏱️ Thời lượng: {media_info.get('duration', 'N/A')} giây")
        print(f"👁️ Lượt xem: {media_info.get('view_count', 'N/A')}")
        
        # Thông tin subtitle
        if "subtitles" in result:
            print(f"\n📝 Subtitle tìm thấy: {len(result['subtitles'])}")
            for lang, subtitle_info in result["subtitles"].items():
                print(f"  🌍 {lang}:")
                print(f"    Định dạng: {subtitle_info.get('ext', 'N/A')}")
                print(f"    URL: {subtitle_info.get('url', 'N/A')}")
                if 'cloud_url' in subtitle_info:
                    print(f"    Cloud URL: {subtitle_info.get('cloud_url', 'N/A')}")
        else:
            print("\n❌ Không tìm thấy subtitle")
        
        print("="*50)

def main():
    parser = argparse.ArgumentParser(
        description="Tải subtitle từ video Bilibili",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ sử dụng:
  python bilibili_subtitle_downloader.py -u "https://www.bilibili.com/video/BV1xx411c7mu"
  python bilibili_subtitle_downloader.py -u "https://www.bilibili.com/video/BV1xx411c7mu" -l zh-Hans en -f xml
  python bilibili_subtitle_downloader.py -u "https://www.bilibili.com/video/BV1xx411c7mu" --save-local ./subtitles
        """
    )
    
    parser.add_argument("-u", "--url", required=True,
                       help="URL của video Bilibili")
    parser.add_argument("-l", "--languages", nargs="+",
                       help="Danh sách ngôn ngữ (vd: zh-Hans en)")
    parser.add_argument("-f", "--format", default="srt",
                       choices=["srt", "vtt", "json3", "xml"],
                       help="Định dạng subtitle (mặc định: srt)")
    parser.add_argument("--no-cloud", action="store_true",
                       help="Không upload lên cloud storage")
    parser.add_argument("--cookie",
                       help="Cookie cho video private")
    parser.add_argument("--save-local",
                       help="Lưu subtitle vào thư mục local")
    parser.add_argument("--api-url", default="http://localhost:5000",
                       help="URL của API server (mặc định: http://localhost:5000)")
    parser.add_argument("--api-key", default="your_api_key_here",
                       help="API key (mặc định: your_api_key_here)")
    
    args = parser.parse_args()
    
    # Kiểm tra URL
    if not args.url.startswith("https://www.bilibili.com/"):
        print("❌ URL không hợp lệ. Phải là URL Bilibili.")
        sys.exit(1)
    
    # Khởi tạo downloader
    downloader = BilibiliSubtitleDownloader(args.api_url, args.api_key)
    
    # Tải subtitle
    result = downloader.download_subtitle(
        video_url=args.url,
        languages=args.languages,
        format=args.format,
        cloud_upload=not args.no_cloud,
        cookie=args.cookie
    )
    
    # In kết quả
    downloader.print_result_summary(result)
    
    # Lưu file local nếu được yêu cầu
    if args.save_local and "error" not in result:
        print(f"\n💾 Đang lưu subtitle vào: {args.save_local}")
        saved_files = downloader.save_subtitle_to_file(result, args.save_local)
        if saved_files:
            print(f"✅ Đã lưu {len(saved_files)} file subtitle")
        else:
            print("❌ Không lưu được file nào")

if __name__ == "__main__":
    main()