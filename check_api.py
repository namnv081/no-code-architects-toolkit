#!/usr/bin/env python3
"""
API Key Checker
Script kiểm tra API key và kết nối tới server
"""

import requests
import sys
import json

def check_api_connection(api_key, base_url="http://localhost:5000"):
    """
    Kiểm tra kết nối API và API key
    
    Args:
        api_key (str): API key để kiểm tra
        base_url (str): URL của API server
    
    Returns:
        bool: True nếu kết nối thành công
    """
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key
    }
    
    # Test với một request đơn giản
    test_payload = {
        "media_url": "https://www.bilibili.com/video/BV1xx411c7mu",
        "subtitles": {
            "download": True,
            "languages": ["zh-CN"],
            "format": "srt"
        }
    }
    
    endpoint = f"{base_url}/v1/BETA/media/download"
    
    print(f"🔍 Đang kiểm tra kết nối tới: {base_url}")
    print(f"🔑 API Key: {api_key[:10]}...")
    
    try:
        # Kiểm tra server có hoạt động không
        health_check_url = f"{base_url}/"
        try:
            health_response = requests.get(health_check_url, timeout=5)
            print(f"✅ Server đang hoạt động (Status: {health_response.status_code})")
        except:
            print("❌ Không thể kết nối tới server")
            return False
        
        # Kiểm tra API key
        response = requests.post(endpoint, headers=headers, json=test_payload, timeout=10)
        
        if response.status_code == 401:
            print("❌ API key không hợp lệ")
            return False
        elif response.status_code == 400:
            print("✅ API key hợp lệ (lỗi request là bình thường cho test)")
            return True
        elif response.status_code in [200, 202]:
            print("✅ API key hợp lệ và server hoạt động tốt")
            result = response.json()
            if result.get('job_id'):
                print(f"📋 Job ID test: {result['job_id']}")
            return True
        else:
            print(f"⚠️  Response không mong đợi (Status: {response.status_code})")
            print(f"📄 Response: {response.text[:200]}...")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ Timeout - Server phản hồi quá chậm")
        return False
    except requests.exceptions.ConnectionError:
        print("❌ Lỗi kết nối - Kiểm tra server có đang chạy không")
        return False
    except Exception as e:
        print(f"❌ Lỗi không xác định: {str(e)}")
        return False

def get_api_key_from_config():
    """
    Thử lấy API key từ file config
    
    Returns:
        str: API key nếu tìm thấy
    """
    try:
        # Thử đọc từ config.py
        import config
        if hasattr(config, 'API_KEY'):
            return config.API_KEY
        elif hasattr(config, 'api_key'):
            return config.api_key
    except:
        pass
    
    try:
        # Thử đọc từ file .env
        with open('.env', 'r') as f:
            for line in f:
                if line.startswith('API_KEY='):
                    return line.split('=', 1)[1].strip()
    except:
        pass
    
    return None

def main():
    """
    Hàm main để chạy script từ command line
    """
    if len(sys.argv) < 2:
        # Thử tự động tìm API key
        auto_api_key = get_api_key_from_config()
        if auto_api_key:
            print(f"🔍 Tìm thấy API key trong config: {auto_api_key[:10]}...")
            api_key = auto_api_key
        else:
            print("🔧 Cách sử dụng:")
            print("   python check_api.py <API_KEY> [base_url]")
            print()
            print("📝 Ví dụ:")
            print("   python check_api.py your_api_key_here")
            print("   python check_api.py your_api_key_here http://localhost:5000")
            print()
            print("💡 Hoặc đặt API_KEY trong file config.py hoặc .env")
            sys.exit(1)
    else:
        api_key = sys.argv[1]
    
    base_url = sys.argv[2] if len(sys.argv) > 2 else "http://localhost:5000"
    
    print("🚀 Bilibili Subtitle Extractor - API Checker")
    print("=" * 50)
    
    if check_api_connection(api_key, base_url):
        print("\n🎉 Kết nối thành công! Bạn có thể sử dụng bilibili_subtitle_extractor.py")
        print("\n📝 Ví dụ sử dụng:")
        print(f"   python bilibili_subtitle_extractor.py {api_key} https://www.bilibili.com/video/BV1xx411c7mu")
    else:
        print("\n❌ Kiểm tra kết nối thất bại")
        print("\n🔧 Hướng dẫn khắc phục:")
        print("1. Đảm bảo API server đang chạy:")
        print("   python app.py")
        print("2. Kiểm tra API key trong file config.py")
        print("3. Kiểm tra URL server (mặc định: http://localhost:5000)")
        sys.exit(1)

if __name__ == "__main__":
    main()