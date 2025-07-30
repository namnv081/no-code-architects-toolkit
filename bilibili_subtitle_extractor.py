#!/usr/bin/env python3
"""
Bilibili Subtitle Extractor
Script để tách subtitle từ video Bilibili sử dụng No-Code Architects Toolkit API
"""

import requests
import json
import sys
import time
from urllib.parse import urlparse

class BilibiliSubtitleExtractor:
    def __init__(self, api_key, base_url="http://localhost:5000"):
        """
        Khởi tạo Bilibili Subtitle Extractor
        
        Args:
            api_key (str): API key để xác thực
            base_url (str): URL của API server (mặc định localhost:5000)
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.headers = {
            'Content-Type': 'application/json',
            'x-api-key': api_key
        }
    
    def extract_subtitles(self, bilibili_url, languages=None, subtitle_format="srt", 
                         webhook_url=None, custom_id=None):
        """
        Tách subtitle từ video Bilibili
        
        Args:
            bilibili_url (str): URL video Bilibili
            languages (list): Danh sách mã ngôn ngữ cần tải (ví dụ: ["zh-CN", "en"])
            subtitle_format (str): Định dạng subtitle ("srt", "vtt", "json3")
            webhook_url (str): URL webhook để nhận kết quả (tùy chọn)
            custom_id (str): ID tùy chỉnh để theo dõi request
            
        Returns:
            dict: Kết quả từ API
        """
        
        # Kiểm tra URL Bilibili hợp lệ
        if not self._is_bilibili_url(bilibili_url):
            raise ValueError("URL không phải là URL Bilibili hợp lệ")
        
        # Chuẩn bị payload
        payload = {
            "media_url": bilibili_url,
            "cloud_upload": True,  # Upload subtitle lên cloud storage
            "subtitles": {
                "download": True,
                "format": subtitle_format,
                "cloud_upload": True
            }
        }
        
        # Thêm ngôn ngữ nếu được chỉ định
        if languages:
            payload["subtitles"]["languages"] = languages
        
        # Thêm webhook URL nếu có
        if webhook_url:
            payload["webhook_url"] = webhook_url
        
        # Thêm custom ID nếu có
        if custom_id:
            payload["id"] = custom_id
        
        # Gửi request đến API
        endpoint = f"{self.base_url}/v1/BETA/media/download"
        
        print(f"🚀 Đang gửi request tới API...")
        print(f"📺 URL video: {bilibili_url}")
        print(f"🌐 Ngôn ngữ: {languages if languages else 'Tất cả có sẵn'}")
        print(f"📄 Định dạng: {subtitle_format}")
        
        try:
            response = requests.post(endpoint, headers=self.headers, json=payload)
            response.raise_for_status()
            
            result = response.json()
            
            if response.status_code == 202:
                print(f"✅ Request đã được queue! Job ID: {result.get('job_id')}")
                if webhook_url:
                    print(f"📞 Kết quả sẽ được gửi tới webhook: {webhook_url}")
                else:
                    print("⏳ Đang xử lý... Vui lòng đợi...")
                    # Nếu không có webhook, có thể cần polling để kiểm tra kết quả
            
            return result
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Lỗi khi gửi request: {str(e)}")
            raise
        except json.JSONDecodeError as e:
            print(f"❌ Lỗi khi parse JSON response: {str(e)}")
            raise
    
    def _is_bilibili_url(self, url):
        """
        Kiểm tra xem URL có phải là URL Bilibili hợp lệ không
        
        Args:
            url (str): URL cần kiểm tra
            
        Returns:
            bool: True nếu là URL Bilibili hợp lệ
        """
        try:
            parsed = urlparse(url)
            bilibili_domains = ['bilibili.com', 'www.bilibili.com', 'b23.tv']
            return any(domain in parsed.netloc for domain in bilibili_domains)
        except:
            return False
    
    def print_subtitle_info(self, result):
        """
        In thông tin subtitle từ kết quả API
        
        Args:
            result (dict): Kết quả từ API
        """
        if result.get('code') == 200 and 'response' in result:
            response_data = result['response']
            
            # Thông tin video
            if 'media' in response_data:
                media = response_data['media']
                print(f"\n📺 Thông tin video:")
                print(f"   Tiêu đề: {media.get('title', 'N/A')}")
                print(f"   Thời lượng: {media.get('duration', 'N/A')} giây")
                print(f"   Người tải lên: {media.get('uploader', 'N/A')}")
                print(f"   Lượt xem: {media.get('view_count', 'N/A')}")
            
            # Thông tin subtitle
            if 'subtitles' in response_data:
                subtitles = response_data['subtitles']
                print(f"\n📄 Subtitle đã tải:")
                
                for lang, subtitle_data in subtitles.items():
                    print(f"   🌐 Ngôn ngữ: {lang}")
                    print(f"      📎 URL: {subtitle_data.get('url', 'N/A')}")
                    print(f"      📋 Định dạng: {subtitle_data.get('ext', 'N/A')}")
                    print()
            else:
                print("❌ Không tìm thấy subtitle nào!")
        
        elif result.get('code') == 202:
            print(f"⏳ Request đang được xử lý. Job ID: {result.get('job_id')}")
        else:
            print(f"❌ Lỗi: {result.get('message', 'Unknown error')}")

def main():
    """
    Hàm main để chạy script từ command line
    """
    if len(sys.argv) < 3:
        print("🔧 Cách sử dụng:")
        print("   python bilibili_subtitle_extractor.py <API_KEY> <BILIBILI_URL> [languages] [format]")
        print()
        print("📝 Ví dụ:")
        print("   python bilibili_subtitle_extractor.py your_api_key https://www.bilibili.com/video/BV1xx411c7mu")
        print("   python bilibili_subtitle_extractor.py your_api_key https://www.bilibili.com/video/BV1xx411c7mu zh-CN,en srt")
        print()
        print("🌐 Ngôn ngữ phổ biến:")
        print("   zh-CN: Tiếng Trung giản thể")
        print("   zh-TW: Tiếng Trung phồn thể") 
        print("   en: Tiếng Anh")
        print("   ja: Tiếng Nhật")
        print("   ko: Tiếng Hàn")
        print()
        print("📄 Định dạng hỗ trợ: srt, vtt, json3")
        sys.exit(1)
    
    api_key = sys.argv[1]
    bilibili_url = sys.argv[2]
    
    # Parse languages nếu có
    languages = None
    if len(sys.argv) > 3 and sys.argv[3]:
        languages = [lang.strip() for lang in sys.argv[3].split(',')]
    
    # Parse format nếu có
    subtitle_format = "srt"
    if len(sys.argv) > 4:
        subtitle_format = sys.argv[4]
    
    # Tạo extractor và chạy
    extractor = BilibiliSubtitleExtractor(api_key)
    
    try:
        result = extractor.extract_subtitles(
            bilibili_url=bilibili_url,
            languages=languages,
            subtitle_format=subtitle_format
        )
        
        extractor.print_subtitle_info(result)
        
        # Lưu kết quả vào file JSON
        output_file = f"bilibili_subtitle_result_{int(time.time())}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        print(f"💾 Kết quả đã được lưu vào: {output_file}")
        
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()