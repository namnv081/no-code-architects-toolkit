#!/usr/bin/env python3
"""
Test example for Bilibili video with danmaku
"""

import requests
import json

def test_danmaku_download():
    """Test downloading danmaku from Bilibili video"""
    
    # API configuration
    base_url = "http://localhost:5000"
    api_key = "your_api_key_here"
    
    # Test with video that has danmaku
    test_data = {
        "media_url": "https://www.bilibili.com/video/BV18Wb1zvEbR",
        "subtitles": {
            "download": True,
            "format": "xml"  # Use XML for danmaku
        },
        "cloud_upload": True
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    try:
        print("🧪 Testing danmaku download...")
        print(f"URL: {base_url}/v1/BETA/media/download")
        print(f"Data: {json.dumps(test_data, indent=2)}")
        print("-" * 50)
        
        response = requests.post(
            f"{base_url}/v1/BETA/media/download",
            headers=headers,
            json=test_data,
            timeout=60
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Success!")
            print(f"Video Title: {result.get('media', {}).get('title', 'N/A')}")
            
            if 'subtitles' in result:
                print(f"Available Subtitles/Danmaku: {list(result['subtitles'].keys())}")
                
                for lang, subtitle_info in result['subtitles'].items():
                    print(f"\n📝 {lang}:")
                    print(f"  Format: {subtitle_info.get('ext', 'N/A')}")
                    print(f"  URL: {subtitle_info.get('url', 'N/A')}")
                    if 'cloud_url' in subtitle_info:
                        print(f"  Cloud URL: {subtitle_info.get('cloud_url', 'N/A')}")
            else:
                print("❌ No subtitles/danmaku found")
        else:
            print(f"❌ Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def test_with_fallback():
    """Test with SRT format that will fallback to available format"""
    
    base_url = "http://localhost:5000"
    api_key = "your_api_key_here"
    
    test_data = {
        "media_url": "https://www.bilibili.com/video/BV18Wb1zvEbR",
        "subtitles": {
            "download": True,
            "format": "srt"  # Request SRT but will fallback to XML
        },
        "cloud_upload": True
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    try:
        print("\n" + "="*50)
        print("🧪 Testing fallback behavior...")
        print("Requesting SRT format but video only has XML danmaku")
        
        response = requests.post(
            f"{base_url}/v1/BETA/media/download",
            headers=headers,
            json=test_data,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Success with fallback!")
            
            if 'subtitles' in result:
                for lang, subtitle_info in result['subtitles'].items():
                    print(f"📝 {lang}: {subtitle_info.get('ext', 'N/A')} format")
                    print(f"   (Requested SRT, got {subtitle_info.get('ext', 'N/A')})")
        else:
            print(f"❌ Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    print("🚀 Bilibili Danmaku Test")
    print("=" * 50)
    
    # Test danmaku download
    test_danmaku_download()
    
    # Test fallback behavior
    test_with_fallback()
    
    print("\n" + "="*50)
    print("✅ Test completed!")
    print("\n💡 Note: This video only has danmaku (bullet comments) in XML format.")
    print("   For videos with actual subtitles, try different video URLs.")