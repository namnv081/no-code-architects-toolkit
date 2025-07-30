#!/usr/bin/env python3
"""
Test script for Bilibili Subtitle Downloader
"""

import sys
import os

# Thêm thư mục hiện tại vào path để import module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bilibili_subtitle_downloader import BilibiliSubtitleDownloader

def test_basic_download():
    """Test tải subtitle cơ bản"""
    
    print("🧪 Test 1: Tải subtitle cơ bản")
    print("-" * 40)
    
    downloader = BilibiliSubtitleDownloader(
        api_url="http://localhost:5000",
        api_key="your_api_key_here"
    )
    
    result = downloader.download_subtitle(
        video_url="https://www.bilibili.com/video/BV18Wb1zvEbR",
        format="xml"  # Video này có danmaku XML
    )
    
    downloader.print_result_summary(result)
    return result

def test_multiple_languages():
    """Test tải subtitle cho nhiều ngôn ngữ"""
    
    print("\n🧪 Test 2: Tải subtitle cho nhiều ngôn ngữ")
    print("-" * 40)
    
    downloader = BilibiliSubtitleDownloader(
        api_url="http://localhost:5000",
        api_key="your_api_key_here"
    )
    
    result = downloader.download_subtitle(
        video_url="https://www.bilibili.com/video/BV18Wb1zvEbR",
        languages=["danmaku"],  # Chỉ tải danmaku
        format="xml"
    )
    
    downloader.print_result_summary(result)
    return result

def test_save_to_file():
    """Test lưu subtitle vào file"""
    
    print("\n🧪 Test 3: Lưu subtitle vào file")
    print("-" * 40)
    
    downloader = BilibiliSubtitleDownloader(
        api_url="http://localhost:5000",
        api_key="your_api_key_here"
    )
    
    result = downloader.download_subtitle(
        video_url="https://www.bilibili.com/video/BV18Wb1zvEbR",
        format="xml"
    )
    
    if "error" not in result:
        # Tạo thư mục test
        test_dir = "./test_subtitles"
        saved_files = downloader.save_subtitle_to_file(result, test_dir)
        
        print(f"✅ Đã lưu {len(saved_files)} file vào {test_dir}")
        for file_path in saved_files:
            print(f"  📁 {file_path}")
    else:
        print("❌ Không thể lưu file do lỗi API")
    
    return result

def test_fallback_format():
    """Test fallback khi định dạng không có sẵn"""
    
    print("\n🧪 Test 4: Test fallback format")
    print("-" * 40)
    
    downloader = BilibiliSubtitleDownloader(
        api_url="http://localhost:5000",
        api_key="your_api_key_here"
    )
    
    # Yêu cầu SRT nhưng video chỉ có XML
    result = downloader.download_subtitle(
        video_url="https://www.bilibili.com/video/BV18Wb1zvEbR",
        format="srt"  # Sẽ fallback sang XML
    )
    
    downloader.print_result_summary(result)
    return result

def test_no_cloud():
    """Test không upload lên cloud storage"""
    
    print("\n🧪 Test 5: Không upload lên cloud storage")
    print("-" * 40)
    
    downloader = BilibiliSubtitleDownloader(
        api_url="http://localhost:5000",
        api_key="your_api_key_here"
    )
    
    result = downloader.download_subtitle(
        video_url="https://www.bilibili.com/video/BV18Wb1zvEbR",
        format="xml",
        cloud_upload=False
    )
    
    downloader.print_result_summary(result)
    return result

def main():
    """Chạy tất cả test"""
    
    print("🚀 Bilibili Subtitle Downloader Test Suite")
    print("=" * 60)
    
    # Kiểm tra API server
    print("🔍 Kiểm tra kết nối API server...")
    try:
        import requests
        response = requests.get("http://localhost:5000/v1/toolkit/test", timeout=5)
        if response.status_code == 200:
            print("✅ API server đang chạy")
        else:
            print("⚠️ API server có thể không hoạt động bình thường")
    except:
        print("❌ Không thể kết nối đến API server")
        print("💡 Hãy đảm bảo API server đang chạy tại http://localhost:5000")
        return
    
    print("\n" + "=" * 60)
    
    # Chạy các test
    tests = [
        test_basic_download,
        test_multiple_languages,
        test_save_to_file,
        test_fallback_format,
        test_no_cloud
    ]
    
    results = []
    for i, test_func in enumerate(tests, 1):
        try:
            print(f"\n📋 Test {i}/{len(tests)}")
            result = test_func()
            results.append(result)
        except Exception as e:
            print(f"❌ Test {i} thất bại: {str(e)}")
            results.append({"error": str(e)})
    
    # Tóm tắt kết quả
    print("\n" + "=" * 60)
    print("📊 TÓM TẮT KẾT QUẢ TEST")
    print("=" * 60)
    
    success_count = 0
    for i, result in enumerate(results, 1):
        if "error" not in result:
            success_count += 1
            print(f"✅ Test {i}: Thành công")
        else:
            print(f"❌ Test {i}: Thất bại - {result['error']}")
    
    print(f"\n🎯 Kết quả: {success_count}/{len(tests)} test thành công")
    
    if success_count == len(tests):
        print("🎉 Tất cả test đều thành công!")
    else:
        print("⚠️ Một số test thất bại. Kiểm tra lại cấu hình API.")

if __name__ == "__main__":
    main()