# 🎬 Tải Subtitle từ Bilibili

Tính năng này cho phép bạn tải subtitle từ video Bilibili một cách dễ dàng và linh hoạt.

## ✨ Tính năng

- ✅ Tải subtitle cho nhiều ngôn ngữ
- ✅ Hỗ trợ các định dạng: SRT, VTT, JSON3
- ✅ Upload tự động lên cloud storage
- ✅ Hỗ trợ video private với cookie
- ✅ Thông tin chi tiết về video
- ✅ Xử lý lỗi thông minh

## 🚀 Cách sử dụng

### 1. Endpoint chính

```
POST /v1/media/bilibili/subtitle
```

### 2. Ví dụ cơ bản

```bash
curl -X POST http://localhost:5000/v1/media/bilibili/subtitle \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "video_url": "https://www.bilibili.com/video/BV1xx411c7mu",
    "languages": ["zh-Hans", "en"],
    "format": "srt"
  }'
```

### 3. Ví dụ Python

```python
import requests

url = "http://localhost:5000/v1/media/bilibili/subtitle"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY"
}

data = {
    "video_url": "https://www.bilibili.com/video/BV1xx411c7mu",
    "languages": ["zh-Hans", "en"],
    "format": "srt"
}

response = requests.post(url, headers=headers, json=data)
result = response.json()

# In kết quả
print(f"Video: {result['video_info']['title']}")
for lang, subtitle in result['subtitles'].items():
    print(f"{lang}: {subtitle['url']}")
```

## 📋 Tham số

| Tham số | Kiểu | Bắt buộc | Mô tả |
|---------|------|----------|-------|
| `video_url` | string | ✅ | URL của video Bilibili |
| `languages` | array | ❌ | Danh sách ngôn ngữ (vd: `["zh-Hans", "en"]`) |
| `format` | string | ❌ | Định dạng subtitle (`srt`, `vtt`, `json3`) |
| `cloud_upload` | boolean | ❌ | Upload lên cloud storage (mặc định: `true`) |
| `cookie` | string | ❌ | Cookie cho video private |

## 🌍 Mã ngôn ngữ

| Mã | Ngôn ngữ |
|----|----------|
| `zh-Hans` | Tiếng Trung giản thể |
| `zh-Hant` | Tiếng Trung phồn thể |
| `en` | Tiếng Anh |
| `ja` | Tiếng Nhật |
| `ko` | Tiếng Hàn |
| `vi` | Tiếng Việt |
| `th` | Tiếng Thái |
| `id` | Tiếng Indonesia |

## 📤 Response

### Success (200)

```json
{
  "video_info": {
    "title": "Tên video",
    "uploader": "Tên uploader",
    "duration": 3600,
    "view_count": 1000000,
    "upload_date": "20240101"
  },
  "subtitles": {
    "zh-Hans": {
      "url": "https://cloud-storage-url/subtitle.srt",
      "ext": "srt",
      "cloud_url": "https://cloud-storage-url/subtitle.srt"
    },
    "en": {
      "url": "https://cloud-storage-url/subtitle_en.srt",
      "ext": "srt",
      "cloud_url": "https://cloud-storage-url/subtitle_en.srt"
    }
  }
}
```

### Error (500)

```json
{
  "message": "Error message",
  "code": 500
}
```

## 🔧 Cài đặt

### 1. Cài đặt dependencies

```bash
pip install -r requirements.txt
```

### 2. Cấu hình environment variables

```bash
export API_KEY="your_api_key"
export S3_ENDPOINT_URL="your_s3_endpoint"
export S3_ACCESS_KEY="your_access_key"
export S3_SECRET_KEY="your_secret_key"
export S3_BUCKET_NAME="your_bucket"
```

### 3. Chạy server

```bash
python app.py
```

## 🧪 Test

Chạy script test:

```bash
python test_bilibili_subtitle.py
```

## 📝 Lưu ý

1. **Video Private**: Cần cookie hợp lệ để tải subtitle từ video private
2. **Định dạng**: SRT là định dạng phổ biến nhất và được khuyến nghị
3. **Cloud Storage**: Subtitle sẽ được upload lên cloud storage nếu `cloud_upload=true`
4. **Ngôn ngữ**: Nếu không chỉ định `languages`, tất cả subtitle có sẵn sẽ được tải

## 🔗 Liên kết

- [Documentation chi tiết](docs/media/bilibili_subtitle.md)
- [API Endpoints khác](README.md)
- [Docker Setup](docker-compose.yml)

## 🤝 Đóng góp

Nếu bạn muốn đóng góp hoặc báo cáo lỗi, vui lòng tạo issue hoặc pull request.

---

**Made with ❤️ for the Bilibili community**