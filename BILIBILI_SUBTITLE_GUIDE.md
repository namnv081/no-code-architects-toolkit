# 🎬 Hướng dẫn tải Subtitle từ Bilibili

Sử dụng API có sẵn `/v1/BETA/media/download` để tải subtitle từ Bilibili.

## 📋 API Endpoint

```
POST /v1/BETA/media/download
```

## 🚀 Cách sử dụng

### 1. Tải tất cả subtitle có sẵn

```bash
curl -X POST http://localhost:5000/v1/BETA/media/download \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "media_url": "https://www.bilibili.com/video/BV1xx411c7mu",
    "subtitles": {
      "download": true,
      "format": "srt"
    }
  }'
```

### 2. Tải subtitle cho ngôn ngữ cụ thể

```bash
curl -X POST http://localhost:5000/v1/BETA/media/download \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "media_url": "https://www.bilibili.com/video/BV1xx411c7mu",
    "subtitles": {
      "download": true,
      "languages": ["zh-Hans", "en"],
      "format": "srt"
    }
  }'
```

### 3. Tải subtitle với cookie (cho video private)

```bash
curl -X POST http://localhost:5000/v1/BETA/media/download \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "media_url": "https://www.bilibili.com/video/BV1xx411c7mu",
    "cookie": "SESSDATA=abc123; bili_jct=def456",
    "subtitles": {
      "download": true,
      "languages": ["zh-Hans"],
      "format": "srt"
    }
  }'
```

## 📝 Ví dụ Python

```python
import requests

url = "http://localhost:5000/v1/BETA/media/download"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY"
}

# Tải subtitle cho ngôn ngữ cụ thể
data = {
    "media_url": "https://www.bilibili.com/video/BV1xx411c7mu",
    "subtitles": {
        "download": True,
        "languages": ["zh-Hans", "en"],
        "format": "srt"
    }
}

response = requests.post(url, headers=headers, json=data)
result = response.json()

# In kết quả
if response.status_code == 200:
    print(f"Video: {result['media']['title']}")
    if 'subtitles' in result:
        for lang, subtitle in result['subtitles'].items():
            print(f"{lang}: {subtitle['url']}")
else:
    print(f"Error: {result}")
```

## 📋 Tham số cho subtitle

| Tham số | Kiểu | Mô tả |
|---------|------|-------|
| `download` | boolean | Bật tải subtitle |
| `languages` | array | Danh sách ngôn ngữ (vd: `["zh-Hans", "en"]`) |
| `format` | string | Định dạng subtitle (`srt`, `vtt`, `json3`) |
| `cloud_upload` | boolean | Upload lên cloud storage |

## 🌍 Mã ngôn ngữ phổ biến

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

## 📤 Response mẫu

```json
{
  "media": {
    "media_url": "https://cloud-storage-url/video.mp4",
    "title": "Tên video",
    "uploader": "Tên uploader",
    "duration": 3600,
    "view_count": 1000000
  },
  "subtitles": {
    "zh-Hans": {
      "url": "https://cloud-storage-url/subtitle.srt",
      "ext": "srt"
    },
    "en": {
      "url": "https://cloud-storage-url/subtitle_en.srt",
      "ext": "srt"
    }
  }
}
```

## 🔧 Các tùy chọn khác

### Tải video + subtitle

```json
{
  "media_url": "https://www.bilibili.com/video/BV1xx411c7mu",
  "subtitles": {
    "download": true,
    "languages": ["zh-Hans", "en"],
    "format": "srt"
  },
  "cloud_upload": true
}
```

### Chỉ tải subtitle (không tải video)

```json
{
  "media_url": "https://www.bilibili.com/video/BV1xx411c7mu",
  "cloud_upload": false,
  "subtitles": {
    "download": true,
    "languages": ["zh-Hans"],
    "format": "srt"
  }
}
```

### Tải với format khác

```json
{
  "media_url": "https://www.bilibili.com/video/BV1xx411c7mu",
  "subtitles": {
    "download": true,
    "languages": ["zh-Hans"],
    "format": "vtt"
  }
}
```

## 📝 Lưu ý

1. **API có sẵn**: Sử dụng `/v1/BETA/media/download` thay vì tạo API mới
2. **Hỗ trợ nhiều nền tảng**: API này hoạt động với Bilibili, YouTube, và nhiều nền tảng khác
3. **Cookie**: Cần cookie hợp lệ cho video private
4. **Cloud Storage**: Subtitle sẽ được upload lên cloud storage nếu `cloud_upload=true`
5. **Định dạng**: SRT là định dạng phổ biến nhất

## 🔗 Liên kết

- [Documentation chi tiết](docs/media/download.md)
- [API Endpoints khác](README.md)
- [Docker Setup](docker-compose.yml)

---

**Sử dụng API có sẵn - Không cần tạo API mới! 🎉**