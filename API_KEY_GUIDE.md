# 🔑 API Key - Hướng Dẫn Chi Tiết

## 📋 API Key là gì?

**API Key** (Application Programming Interface Key) là một mã định danh duy nhất được sử dụng để xác thực và ủy quyền truy cập vào API. Trong hệ thống Bilibili Subtitle Extractor này, API key đóng vai trò như một "chìa khóa" để:

- ✅ **Xác thực**: Chứng minh bạn có quyền sử dụng API
- ✅ **Bảo mật**: Ngăn chặn truy cập trái phép
- ✅ **Theo dõi**: Giám sát việc sử dụng API
- ✅ **Kiểm soát**: Giới hạn quyền truy cập

## 🎯 API Key của bạn

Tôi đã tạo API key cho bạn:

```
bili_sub_U5zwRcs3F2Z8zSv3jr4h0w
```

API key này đã được:
- ✅ Lưu vào file `.env`
- ✅ Thiết lập trong environment variable
- ✅ Sẵn sàng sử dụng

## 🛠️ Cách sử dụng API Key

### 1. Sử dụng trực tiếp trong command line

```bash
# Tách subtitle từ Bilibili
python3 bilibili_subtitle_extractor.py bili_sub_U5zwRcs3F2Z8zSv3jr4h0w https://www.bilibili.com/video/BV1xx411c7mu

# Kiểm tra kết nối API
python3 check_api.py bili_sub_U5zwRcs3F2Z8zSv3jr4h0w
```

### 2. Sử dụng environment variable

```bash
# Thiết lập API key (đã làm rồi)
export API_KEY=bili_sub_U5zwRcs3F2Z8zSv3jr4h0w

# Sử dụng với script tự động nhận API key từ environment
python3 check_api.py
```

### 3. Sử dụng trong Python code

```python
import os
from bilibili_subtitle_extractor import BilibiliSubtitleExtractor

# Lấy API key từ environment variable
api_key = os.environ.get('API_KEY', 'bili_sub_U5zwRcs3F2Z8zSv3jr4h0w')

# Tạo extractor
extractor = BilibiliSubtitleExtractor(api_key)

# Tách subtitle
result = extractor.extract_subtitles("https://www.bilibili.com/video/BV1xx411c7mu")
```

## 📁 Các cách lưu trữ API Key

### 1. File .env (Khuyến nghị)

File `.env` trong thư mục hiện tại:
```
API_KEY=bili_sub_U5zwRcs3F2Z8zSv3jr4h0w
```

### 2. Environment Variable

```bash
# Thiết lập tạm thời (chỉ cho session hiện tại)
export API_KEY=bili_sub_U5zwRcs3F2Z8zSv3jr4h0w

# Thiết lập vĩnh viễn (thêm vào ~/.bashrc)
echo 'export API_KEY=bili_sub_U5zwRcs3F2Z8zSv3jr4h0w' >> ~/.bashrc
source ~/.bashrc
```

### 3. Config file (cho development)

Có thể thêm vào `config.py`:
```python
API_KEY = "bili_sub_U5zwRcs3F2Z8zSv3jr4h0w"
```

## 🔒 Bảo mật API Key

### ⚠️ Những điều KHÔNG nên làm:

- ❌ **Không** commit API key vào Git repository
- ❌ **Không** chia sẻ API key công khai
- ❌ **Không** hardcode API key trong source code
- ❌ **Không** gửi API key qua email/chat không mã hóa

### ✅ Những điều NÊN làm:

- ✅ **Lưu** API key trong file `.env` (đã thêm vào `.gitignore`)
- ✅ **Sử dụng** environment variables
- ✅ **Tạo** API key khác nhau cho các môi trường (dev/prod)
- ✅ **Thay đổi** API key định kỳ

## 🔧 Tạo API Key mới

### Cách 1: Sử dụng script setup

```bash
python3 setup_api_key.py
```

### Cách 2: Tạo thủ công

```bash
# Tạo API key ngẫu nhiên
python3 -c "import secrets; print('bili_sub_' + secrets.token_urlsafe(16))"

# Lưu vào .env
echo "API_KEY=your_new_api_key" > .env
```

### Cách 3: Tùy chỉnh

Bạn có thể tạo API key theo ý muốn, ví dụ:
```
my_custom_api_key_2024
bilibili_extractor_secret_key
user_john_api_key_v1
```

## 🚀 Test API Key

### Kiểm tra nhanh

```bash
# Test kết nối
python3 check_api.py bili_sub_U5zwRcs3F2Z8zSv3jr4h0w

# Test với environment variable
python3 check_api.py
```

### Kết quả mong đợi

```
🔍 Đang kiểm tra kết nối tới: http://localhost:5000
🔑 API Key: bili_sub_U...
✅ Server đang hoạt động (Status: 200)
✅ API key hợp lệ và server hoạt động tốt
🎉 Kết nối thành công!
```

## 🐛 Troubleshooting

### Lỗi "Invalid API key"

```bash
# Kiểm tra API key hiện tại
echo $API_KEY

# Thiết lập lại API key
export API_KEY=bili_sub_U5zwRcs3F2Z8zSv3jr4h0w

# Hoặc tạo API key mới
python3 setup_api_key.py
```

### Lỗi "API key not found"

```bash
# Tạo file .env
echo "API_KEY=bili_sub_U5zwRcs3F2Z8zSv3jr4h0w" > .env

# Hoặc thiết lập environment variable
export API_KEY=bili_sub_U5zwRcs3F2Z8zSv3jr4h0w
```

### Server không nhận API key

1. **Kiểm tra server đang chạy**:
   ```bash
   curl http://localhost:5000/
   ```

2. **Kiểm tra header request**:
   ```bash
   curl -H "x-api-key: bili_sub_U5zwRcs3F2Z8zSv3jr4h0w" http://localhost:5000/v1/BETA/media/download
   ```

## 📊 Ví dụ hoàn chỉnh

```bash
# 1. Thiết lập API key
export API_KEY=bili_sub_U5zwRcs3F2Z8zSv3jr4h0w

# 2. Khởi động server (terminal 1)
python3 app.py

# 3. Test API key (terminal 2)
python3 check_api.py

# 4. Tách subtitle
python3 bilibili_subtitle_extractor.py $API_KEY https://www.bilibili.com/video/BV1xx411c7mu zh-CN,en

# 5. Tải subtitle
python3 download_subtitles.py bilibili_subtitle_result_*.json
```

## 💡 Tips

1. **Backup API key**: Lưu API key ở nơi an toàn
2. **Multiple keys**: Có thể tạo nhiều API key cho các mục đích khác nhau
3. **Monitoring**: Theo dõi việc sử dụng API key
4. **Rotation**: Thay đổi API key định kỳ để tăng bảo mật

---

🎉 **Bây giờ bạn đã hiểu rõ về API key và sẵn sàng sử dụng Bilibili Subtitle Extractor!**