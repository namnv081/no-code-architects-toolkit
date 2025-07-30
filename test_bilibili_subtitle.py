#!/usr/bin/env python3
"""
Test script for Bilibili subtitle download endpoint
"""

import requests
import json
import sys

def test_bilibili_subtitle_download():
    """Test the Bilibili subtitle download endpoint"""
    
    # API configuration
    base_url = "http://localhost:5000"  # Change this to your API URL
    api_key = "your_api_key_here"  # Change this to your API key
    
    # Test data
    test_data = {
        "video_url": "https://www.bilibili.com/video/BV1xx411c7mu",  # Example Bilibili URL
        "languages": ["zh-Hans", "en"],  # Chinese simplified and English
        "format": "srt",
        "cloud_upload": True
    }
    
    # Headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    try:
        print("Testing Bilibili subtitle download...")
        print(f"URL: {base_url}/v1/media/bilibili/subtitle")
        print(f"Data: {json.dumps(test_data, indent=2)}")
        print("-" * 50)
        
        # Make the request
        response = requests.post(
            f"{base_url}/v1/media/bilibili/subtitle",
            headers=headers,
            json=test_data,
            timeout=60
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        print("-" * 50)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Success!")
            print(f"Video Title: {result.get('video_info', {}).get('title', 'N/A')}")
            print(f"Available Subtitles: {list(result.get('subtitles', {}).keys())}")
            
            # Print subtitle details
            for lang, subtitle_info in result.get('subtitles', {}).items():
                print(f"\n📝 {lang}:")
                print(f"  Format: {subtitle_info.get('ext', 'N/A')}")
                print(f"  URL: {subtitle_info.get('url', 'N/A')}")
                if 'cloud_url' in subtitle_info:
                    print(f"  Cloud URL: {subtitle_info.get('cloud_url', 'N/A')}")
                    
        else:
            print("❌ Error!")
            print(f"Error Message: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Make sure the API server is running")
    except requests.exceptions.Timeout:
        print("❌ Timeout: Request took too long")
    except Exception as e:
        print(f"❌ Unexpected Error: {str(e)}")

def test_without_languages():
    """Test downloading all available subtitles"""
    
    base_url = "http://localhost:5000"
    api_key = "your_api_key_here"
    
    test_data = {
        "video_url": "https://www.bilibili.com/video/BV1xx411c7mu",
        "format": "srt"
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    try:
        print("\n" + "="*50)
        print("Testing download of all available subtitles...")
        
        response = requests.post(
            f"{base_url}/v1/media/bilibili/subtitle",
            headers=headers,
            json=test_data,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Success!")
            print(f"All available subtitles: {list(result.get('subtitles', {}).keys())}")
        else:
            print(f"❌ Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    print("🚀 Bilibili Subtitle Download Test")
    print("=" * 50)
    
    # Test with specific languages
    test_bilibili_subtitle_download()
    
    # Test without specifying languages (download all)
    test_without_languages()
    
    print("\n" + "="*50)
    print("Test completed!")