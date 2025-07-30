#!/usr/bin/env python3
"""
Bilibili Danmaku Extractor
Script để tách danmaku (comments/barrage) từ video Bilibili
"""

import subprocess
import sys
import os
from pathlib import Path
import argparse

def extract_bilibili_danmaku(url, output_dir="danmaku_output"):
    """
    Tách danmaku từ video Bilibili
    
    Args:
        url (str): URL video Bilibili
        output_dir (str): Thư mục lưu danmaku
    
    Returns:
        dict: Thông tin về danmaku đã tách
    """
    print(f"🎯 Đang tách danmaku từ: {url}")
    
    # Tạo thư mục output
    Path(output_dir).mkdir(exist_ok=True)
    
    # Command yt-dlp để tải danmaku
    cmd = [
        "yt-dlp",
        "--write-subs",           # Tải subtitle/danmaku
        "--sub-langs", "danmaku", # Chỉ lấy danmaku
        "--skip-download",        # Không tải video, chỉ tải danmaku
        "--output", f"{output_dir}/%(title)s.%(ext)s",
        url
    ]
    
    print("🔄 Đang tải danmaku...")
    print(f"Command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print("✅ Tải danmaku thành công!")
            
            # Tìm files đã tải
            danmaku_files = list(Path(output_dir).glob("*.xml"))
            
            info = {
                "status": "success",
                "url": url,
                "output_dir": output_dir,
                "danmaku_files": [str(f) for f in danmaku_files],
                "total_files": len(danmaku_files)
            }
            
            print(f"📁 Thư mục output: {output_dir}")
            print(f"📄 Số file danmaku: {len(danmaku_files)}")
            
            for file in danmaku_files:
                print(f"   - {file.name}")
                
            return info
            
        else:
            print("❌ Lỗi khi tải danmaku:")
            print(result.stderr)
            return {
                "status": "error",
                "error": result.stderr,
                "url": url
            }
            
    except subprocess.TimeoutExpired:
        print("⏰ Timeout - quá trình tải mất quá nhiều thời gian")
        return {
            "status": "timeout",
            "url": url
        }
    except Exception as e:
        print(f"💥 Lỗi: {e}")
        return {
            "status": "exception",
            "error": str(e),
            "url": url
        }

def list_available_subtitles(url):
    """
    Liệt kê tất cả subtitle/danmaku có sẵn
    """
    print(f"🔍 Kiểm tra subtitle có sẵn cho: {url}")
    
    cmd = ["yt-dlp", "--list-subs", url]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("✅ Danh sách subtitle/danmaku:")
            print(result.stdout)
        else:
            print("❌ Lỗi:")
            print(result.stderr)
            
    except Exception as e:
        print(f"💥 Lỗi: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Tách danmaku từ video Bilibili",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ:
  python3 bilibili_danmaku_extractor.py https://www.bilibili.com/video/BV1xx411c7mu
  python3 bilibili_danmaku_extractor.py --list https://www.bilibili.com/video/BV1xx411c7mu
  python3 bilibili_danmaku_extractor.py --output my_danmaku https://www.bilibili.com/video/BV1xx411c7mu
        """
    )
    
    parser.add_argument("url", help="URL video Bilibili")
    parser.add_argument("--output", "-o", default="danmaku_output", 
                       help="Thư mục lưu danmaku (mặc định: danmaku_output)")
    parser.add_argument("--list", "-l", action="store_true",
                       help="Chỉ liệt kê subtitle có sẵn, không tải")
    
    args = parser.parse_args()
    
    print("🚀 Bilibili Danmaku Extractor")
    print("=" * 40)
    
    if args.list:
        list_available_subtitles(args.url)
    else:
        result = extract_bilibili_danmaku(args.url, args.output)
        
        if result["status"] == "success":
            print(f"\n🎉 Hoàn thành! Danmaku đã được lưu vào: {args.output}")
            print("\n💡 Lưu ý: Danmaku là các comment hiển thị trên video,")
            print("   không phải subtitle thông thường. File XML chứa")
            print("   các comment của người xem với thời gian hiển thị.")
        else:
            print(f"\n❌ Không thể tải danmaku: {result.get('error', 'Unknown error')}")
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Nếu không có args, chạy demo
        demo_url = "https://www.bilibili.com/video/BV1xx411c7mu"
        print("🎯 Demo mode - sử dụng URL test")
        print(f"URL: {demo_url}")
        print("\nKiểm tra subtitle có sẵn:")
        list_available_subtitles(demo_url)
        print("\n" + "="*50)
        print("Tải danmaku:")
        extract_bilibili_danmaku(demo_url)
    else:
        main()