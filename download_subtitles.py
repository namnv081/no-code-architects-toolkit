#!/usr/bin/env python3
"""
Download Subtitles Helper
Script hỗ trợ tải subtitle từ cloud URL và lưu vào file local
"""

import requests
import json
import os
import sys
from urllib.parse import urlparse
import re

def download_subtitle_from_url(url, output_path, filename=None):
    """
    Tải subtitle từ URL và lưu vào file
    
    Args:
        url (str): URL của subtitle
        output_path (str): Thư mục để lưu file
        filename (str): Tên file (tùy chọn)
    
    Returns:
        str: Đường dẫn file đã lưu
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Tự động xác định tên file nếu không được cung cấp
        if not filename:
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename or '.' not in filename:
                filename = "subtitle.srt"
        
        # Đảm bảo thư mục output tồn tại
        os.makedirs(output_path, exist_ok=True)
        
        # Đường dẫn file đầy đủ
        file_path = os.path.join(output_path, filename)
        
        # Lưu file
        with open(file_path, 'wb') as f:
            f.write(response.content)
        
        print(f"✅ Đã tải subtitle: {file_path}")
        return file_path
        
    except Exception as e:
        print(f"❌ Lỗi khi tải subtitle từ {url}: {str(e)}")
        return None

def process_bilibili_result(json_file_path, output_dir="subtitles"):
    """
    Xử lý file JSON kết quả từ Bilibili extractor và tải tất cả subtitle
    
    Args:
        json_file_path (str): Đường dẫn file JSON kết quả
        output_dir (str): Thư mục để lưu subtitle
    """
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            result = json.load(f)
        
        if result.get('code') != 200:
            print(f"❌ Kết quả không thành công: {result.get('message', 'Unknown error')}")
            return
        
        response_data = result.get('response', {})
        subtitles = response_data.get('subtitles', {})
        
        if not subtitles:
            print("❌ Không tìm thấy subtitle trong kết quả")
            return
        
        # Lấy thông tin video để tạo tên thư mục
        media_info = response_data.get('media', {})
        video_title = media_info.get('title', 'unknown_video')
        
        # Làm sạch tên file (loại bỏ ký tự không hợp lệ)
        safe_title = re.sub(r'[<>:"/\\|?*]', '_', video_title)
        video_output_dir = os.path.join(output_dir, safe_title)
        
        print(f"📺 Video: {video_title}")
        print(f"📁 Lưu vào thư mục: {video_output_dir}")
        print()
        
        downloaded_files = []
        
        for lang, subtitle_data in subtitles.items():
            subtitle_url = subtitle_data.get('url')
            if not subtitle_url:
                print(f"⚠️  Không có URL cho subtitle {lang}")
                continue
            
            # Tạo tên file với mã ngôn ngữ
            ext = subtitle_data.get('ext', 'srt')
            filename = f"{safe_title}.{lang}.{ext}"
            
            print(f"🌐 Đang tải subtitle {lang}...")
            file_path = download_subtitle_from_url(subtitle_url, video_output_dir, filename)
            
            if file_path:
                downloaded_files.append(file_path)
                
                # Hiển thị preview nội dung subtitle
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        lines = content.split('\n')[:10]  # Hiển thị 10 dòng đầu
                        print(f"   📄 Preview ({len(content.split())} từ):")
                        for line in lines:
                            if line.strip():
                                print(f"      {line}")
                        if len(content.split('\n')) > 10:
                            print("      ...")
                except:
                    pass
                print()
        
        if downloaded_files:
            print(f"🎉 Đã tải thành công {len(downloaded_files)} file subtitle:")
            for file_path in downloaded_files:
                print(f"   📄 {file_path}")
        else:
            print("❌ Không tải được file subtitle nào")
            
    except Exception as e:
        print(f"❌ Lỗi khi xử lý file JSON: {str(e)}")

def main():
    """
    Hàm main để chạy script từ command line
    """
    if len(sys.argv) < 2:
        print("🔧 Cách sử dụng:")
        print("   python download_subtitles.py <JSON_RESULT_FILE> [output_directory]")
        print()
        print("📝 Ví dụ:")
        print("   python download_subtitles.py bilibili_subtitle_result_1234567890.json")
        print("   python download_subtitles.py bilibili_subtitle_result_1234567890.json my_subtitles")
        print()
        print("📁 Mặc định subtitle sẽ được lưu vào thư mục 'subtitles'")
        sys.exit(1)
    
    json_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "subtitles"
    
    if not os.path.exists(json_file):
        print(f"❌ File không tồn tại: {json_file}")
        sys.exit(1)
    
    print(f"📂 Đang xử lý file: {json_file}")
    print(f"📁 Thư mục output: {output_dir}")
    print()
    
    process_bilibili_result(json_file, output_dir)

if __name__ == "__main__":
    main()