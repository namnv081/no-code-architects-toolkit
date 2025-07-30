#!/usr/bin/env python3

import sys
import subprocess
import os

def test_bilibili_subtitle():
    """Test tách subtitle từ Bilibili"""
    
    print("🎯 Test Tách Subtitle Bilibili")
    print("=" * 40)
    
    # Test URL Bilibili
    test_url = "https://www.bilibili.com/video/BV1xx411c7mu"
    
    print(f"📹 Test URL: {test_url}")
    
    # Tạo thư mục output
    os.makedirs("test_output", exist_ok=True)
    
    # Command yt-dlp để test
    cmd = [
        "yt-dlp",
        "--list-subs",  # Chỉ list subtitle, không tải
        test_url
    ]
    
    print("🔍 Kiểm tra subtitle có sẵn...")
    print(f"Command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("✅ Thành công! Danh sách subtitle:")
            print(result.stdout)
        else:
            print("❌ Lỗi:")
            print(result.stderr)
            
    except subprocess.TimeoutExpired:
        print("⏰ Timeout - có thể do network hoặc URL không hợp lệ")
    except Exception as e:
        print(f"💥 Lỗi: {e}")

if __name__ == "__main__":
    test_bilibili_subtitle()