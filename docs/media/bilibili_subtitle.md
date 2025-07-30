# Bilibili Subtitle Download

Tải subtitle từ video Bilibili với các tùy chọn linh hoạt.

## Endpoint

```
POST /v1/media/bilibili/subtitle
```

## Mô tả

Endpoint này cho phép bạn tải subtitle từ video Bilibili. Nó hỗ trợ:
- Tải subtitle cho nhiều ngôn ngữ
- Chọn định dạng subtitle (SRT, VTT, JSON3)
- Upload subtitle lên cloud storage
- Hỗ trợ cookie cho video private

## Tham số

| Tham số | Kiểu | Bắt buộc | Mô tả |
|---------|------|----------|-------|
| `video_url` | string | Có | URL của video Bilibili |
| `languages` | array | Không | Danh sách ngôn ngữ subtitle (vd: `["zh-Hans", "en", "vi"]`) |
| `format` | string | Không | Định dạng subtitle (`srt`, `vtt`, `json3`). Mặc định: `srt` |
| `cloud_upload` | boolean | Không | Có upload lên cloud storage không. Mặc định: `true` |
| `cookie` | string | Không | Cookie để truy cập video private |

## Ví dụ Request

### Tải tất cả subtitle có sẵn

```json
{
  "video_url": "https://www.bilibili.com/video/BV1xx411c7mu"
}
```

### Tải subtitle cho ngôn ngữ cụ thể

```json
{
  "video_url": "https://www.bilibili.com/video/BV1xx411c7mu",
  "languages": ["zh-Hans", "en"],
  "format": "srt"
}
```

### Tải subtitle với cookie (cho video private)

```json
{
  "video_url": "https://www.bilibili.com/video/BV1xx411c7mu",
  "languages": ["zh-Hans"],
  "format": "srt",
  "cookie": "SESSDATA=abc123; bili_jct=def456"
}
```

## Response

### Success Response (200)

```json
{
  "video_info": {
    "title": "Tên video",
    "uploader": "Tên uploader",
    "duration": 3600,
    "view_count": 1000000,
    "upload_date": "20240101",
    "description": "Mô tả video"
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

### Error Response (500)

```json
{
  "message": "Error message",
  "code": 500
}
```

## Mã ngôn ngữ phổ biến

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

## Lưu ý

1. **Video Private**: Để tải subtitle từ video private, bạn cần cung cấp cookie hợp lệ
2. **Định dạng Subtitle**: 
   - `srt`: SubRip Subtitle (phổ biến nhất)
   - `vtt`: Web Video Text Tracks
   - `json3`: YouTube's JSON format
3. **Cloud Upload**: Nếu `cloud_upload` là `true`, subtitle sẽ được upload lên cloud storage và URL sẽ được trả về
4. **Ngôn ngữ**: Nếu không chỉ định `languages`, tất cả subtitle có sẵn sẽ được tải

## Ví dụ sử dụng với cURL

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

## Ví dụ sử dụng với Python

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
print(response.json())
```