#!/usr/bin/env python3
"""
API Key Setup Helper
Script giúp thiết lập API key cho Bilibili Subtitle Extractor
"""

import os
import sys
import uuid
import secrets

def generate_api_key():
    """
    Tạo API key ngẫu nhiên
    
    Returns:
        str: API key được tạo
    """
    # Tạo API key với format: prefix + random string
    prefix = "bili_sub_"
    random_part = secrets.token_urlsafe(16)
    return f"{prefix}{random_part}"

def save_api_key_to_env(api_key):
    """
    Lưu API key vào file .env
    
    Args:
        api_key (str): API key cần lưu
    """
    env_content = f"# Bilibili Subtitle Extractor API Key\nAPI_KEY={api_key}\n"
    
    # Kiểm tra xem file .env đã tồn tại chưa
    if os.path.exists('.env'):
        # Đọc nội dung hiện tại
        with open('.env', 'r') as f:
            existing_content = f.read()
        
        # Kiểm tra xem đã có API_KEY chưa
        lines = existing_content.split('\n')
        new_lines = []
        api_key_found = False
        
        for line in lines:
            if line.startswith('API_KEY='):
                new_lines.append(f"API_KEY={api_key}")
                api_key_found = True
            else:
                new_lines.append(line)
        
        # Nếu chưa có API_KEY, thêm vào
        if not api_key_found:
            new_lines.append(f"API_KEY={api_key}")
        
        env_content = '\n'.join(new_lines)
    
    # Lưu vào file .env
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print(f"✅ Đã lưu API key vào file .env")

def export_api_key_to_shell(api_key):
    """
    Tạo lệnh export cho shell
    
    Args:
        api_key (str): API key cần export
    """
    print(f"\n🔧 Để sử dụng API key trong session hiện tại, chạy:")
    print(f"export API_KEY={api_key}")
    print(f"\n💡 Hoặc thêm vào ~/.bashrc để sử dụng vĩnh viễn:")
    print(f"echo 'export API_KEY={api_key}' >> ~/.bashrc")

def check_current_api_key():
    """
    Kiểm tra API key hiện tại
    
    Returns:
        str: API key hiện tại hoặc None
    """
    # Kiểm tra từ environment variable
    env_api_key = os.environ.get('API_KEY')
    if env_api_key:
        return env_api_key
    
    # Kiểm tra từ file .env
    if os.path.exists('.env'):
        with open('.env', 'r') as f:
            for line in f:
                if line.startswith('API_KEY='):
                    return line.split('=', 1)[1].strip()
    
    return None

def main():
    """
    Hàm main
    """
    print("🔑 API Key Setup Helper")
    print("=" * 40)
    
    # Kiểm tra API key hiện tại
    current_key = check_current_api_key()
    if current_key:
        print(f"🔍 API key hiện tại: {current_key[:15]}...")
        
        choice = input("\n❓ Bạn có muốn tạo API key mới không? (y/N): ").lower()
        if choice not in ['y', 'yes']:
            print(f"\n✅ Sử dụng API key hiện tại: {current_key}")
            export_api_key_to_shell(current_key)
            return
    
    print("\n📋 Lựa chọn:")
    print("1. Tạo API key ngẫu nhiên (khuyến nghị)")
    print("2. Nhập API key tùy chỉnh")
    print("3. Sử dụng API key demo (chỉ để test)")
    
    choice = input("\n❓ Chọn tùy chọn (1-3): ").strip()
    
    if choice == "1":
        # Tạo API key ngẫu nhiên
        api_key = generate_api_key()
        print(f"\n🎲 Đã tạo API key ngẫu nhiên: {api_key}")
        
    elif choice == "2":
        # Nhập API key tùy chỉnh
        api_key = input("\n📝 Nhập API key của bạn: ").strip()
        if not api_key:
            print("❌ API key không được để trống!")
            sys.exit(1)
        print(f"\n✅ Đã nhận API key: {api_key}")
        
    elif choice == "3":
        # Sử dụng API key demo
        api_key = "demo_api_key_12345"
        print(f"\n🧪 Sử dụng API key demo: {api_key}")
        print("⚠️  Lưu ý: API key demo chỉ dùng để test, không hoạt động với server thật")
        
    else:
        print("❌ Lựa chọn không hợp lệ!")
        sys.exit(1)
    
    # Lưu API key
    save_api_key_to_env(api_key)
    export_api_key_to_shell(api_key)
    
    print(f"\n🎉 Thiết lập hoàn tất!")
    print(f"\n📝 Bước tiếp theo:")
    print(f"1. Khởi động API server: python3 app.py")
    print(f"2. Kiểm tra kết nối: python3 check_api.py {api_key}")
    print(f"3. Tách subtitle: python3 bilibili_subtitle_extractor.py {api_key} <BILIBILI_URL>")

if __name__ == "__main__":
    main()