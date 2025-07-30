#!/bin/bash

# Bilibili Subtitle Extractor - Demo Script
# Script khởi động nhanh để demo công cụ tách subtitle

echo "🚀 Bilibili Subtitle Extractor - Demo"
echo "======================================"

# Kiểm tra Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 không được tìm thấy. Vui lòng cài đặt Python3."
    exit 1
fi

# Kiểm tra pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 không được tìm thấy. Vui lòng cài đặt pip3."
    exit 1
fi

# Cài đặt dependencies nếu cần
echo "📦 Kiểm tra dependencies..."
if [ ! -f "requirements.txt" ]; then
    echo "❌ File requirements.txt không tồn tại"
    exit 1
fi

# Cài đặt packages cần thiết cho script
echo "📦 Cài đặt packages cho script..."
pip3 install requests urllib3 > /dev/null 2>&1

# Tạo API key demo nếu chưa có
if [ -z "$API_KEY" ]; then
    echo "🔑 Tạo API key demo..."
    export API_KEY="demo_api_key_12345"
    echo "   API Key demo: $API_KEY"
    echo "   (Trong thực tế, bạn cần API key thật từ server)"
fi

# Tạo thư mục output
mkdir -p subtitles

echo ""
echo "✅ Chuẩn bị hoàn tất!"
echo ""
echo "🔧 Cách sử dụng:"
echo "1. Khởi động API server (nếu chưa chạy):"
echo "   python3 app.py"
echo ""
echo "2. Kiểm tra kết nối API:"
echo "   python3 check_api.py $API_KEY"
echo ""
echo "3. Tách subtitle từ Bilibili:"
echo "   python3 bilibili_subtitle_extractor.py $API_KEY https://www.bilibili.com/video/BV1xx411c7mu"
echo ""
echo "4. Tải subtitle về máy:"
echo "   python3 download_subtitles.py bilibili_subtitle_result_*.json"
echo ""
echo "📝 Ví dụ URL Bilibili:"
echo "   - https://www.bilibili.com/video/BV1xx411c7mu"
echo "   - https://b23.tv/shortlink"
echo ""
echo "🌐 Ngôn ngữ phổ biến:"
echo "   - zh-CN (Tiếng Trung giản thể)"
echo "   - zh-TW (Tiếng Trung phồn thể)"
echo "   - en (Tiếng Anh)"
echo "   - ja (Tiếng Nhật)"
echo ""
echo "📄 Định dạng hỗ trợ: srt, vtt, json3"
echo ""

# Kiểm tra xem có file app.py không
if [ -f "app.py" ]; then
    echo "💡 Để khởi động API server, chạy:"
    echo "   python3 app.py"
    echo ""
    echo "🔍 Để kiểm tra server đang chạy:"
    echo "   curl http://localhost:5000/"
else
    echo "⚠️  File app.py không tồn tại. Đảm bảo bạn đang ở thư mục đúng."
fi

echo ""
echo "📚 Đọc README_Bilibili_Subtitle_Extractor.md để biết thêm chi tiết"