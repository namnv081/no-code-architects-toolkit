# 🎬 Hướng dẫn lấy Subtitle từ YouTube bằng No-Code Architects Toolkit API

## 📋 **Tổng quan**
API này cung cấp 2 cách để lấy subtitle từ video YouTube:

1. **Phương pháp A**: Download subtitle có sẵn từ YouTube (nhanh)
2. **Phương pháp B**: Transcribe audio thành text (chính xác hơn, chậm hơn)

---

## 🚀 **Phương pháp A: Download Subtitle có sẵn từ YouTube**

### **API Endpoint**: `/v1/BETA/media/download`

```bash
curl -X POST "http://localhost:8080/v1/BETA/media/download" \
  -H "x-api-key: demo-test-api-key-123" \
  -H "Content-Type: application/json" \
  -d '{
    "media_url": "https://www.youtube.com/watch?v=VIDEO_ID",
    "id": "youtube-subtitle-download",
    "cloud_upload": false,
    "subtitles": {
      "download": true,
      "languages": ["en", "vi", "es"],
      "format": "srt",
      "cloud_upload": false
    }
  }'
```

### **Tham số quan trọng:**
- `media_url`: URL video YouTube
- `subtitles.download`: `true` để tải subtitle
- `subtitles.languages`: Mảng các ngôn ngữ cần tải (["en", "vi", "es"])
- `subtitles.format`: Format subtitle ("srt", "vtt", "json3")
- `cloud_upload`: `false` để nhận kết quả trực tiếp

### **Response thành công:**
```json
{
  "code": 200,
  "response": {
    "subtitles": [
      {
        "language": "en",
        "subtitle_url": "https://storage.example.com/subtitles_en.srt",
        "format": "srt"
      }
    ]
  }
}
```

---

## 🎤 **Phương pháp B: Transcribe Audio thành Text**

### **Bước 1: Download audio từ YouTube**
```bash
curl -X POST "http://localhost:8080/v1/BETA/media/download" \
  -H "x-api-key: demo-test-api-key-123" \
  -H "Content-Type: application/json" \
  -d '{
    "media_url": "https://www.youtube.com/watch?v=VIDEO_ID",
    "id": "youtube-audio-download",
    "cloud_upload": false,
    "audio": {
      "extract": true,
      "format": "mp3"
    }
  }'
```

### **Bước 2: Transcribe audio thành subtitle**
```bash
curl -X POST "http://localhost:8080/v1/media/transcribe" \
  -H "x-api-key: demo-test-api-key-123" \
  -H "Content-Type: application/json" \
  -d '{
    "media_url": "URL_AUDIO_TỪ_BƯỚC_1",
    "task": "transcribe",
    "include_text": true,
    "include_srt": true,
    "include_segments": true,
    "language": "en",
    "id": "audio-transcribe"
  }'
```

---

## 🔧 **Giải quyết vấn đề YouTube Bot Detection**

### **Vấn đề hiện tại:**
```
ERROR: Sign in to confirm you're not a bot. Use --cookies-from-browser or --cookies
```

### **Giải pháp 1: Sử dụng Cookies**
```bash
curl -X POST "http://localhost:8080/v1/BETA/media/download" \
  -H "x-api-key: demo-test-api-key-123" \
  -H "Content-Type: application/json" \
  -d '{
    "media_url": "https://www.youtube.com/watch?v=VIDEO_ID",
    "cookie": "# Netscape HTTP Cookie File\n.youtube.com\tTRUE\t/\tFALSE\t0\tCONSENT\tYES+cb",
    "subtitles": {
      "download": true,
      "languages": ["en"],
      "format": "srt"
    }
  }'
```

### **Giải pháp 2: Sử dụng video từ nguồn khác**
- **Vimeo**: `https://vimeo.com/VIDEO_ID`
- **Direct links**: `https://example.com/video.mp4`
- **Podcast**: `https://example.com/podcast.mp3`

---

## 🧪 **Demo thực tế với file audio mẫu**

### **Test với file audio có speech:**
```bash
# Tạo file audio test
echo "Hello world, this is a test audio file" | \
  espeak -s 150 -w /tmp/test_audio.wav

# Upload file lên server tạm
# (Trong thực tế, bạn cần upload lên cloud storage)

# Transcribe
curl -X POST "http://localhost:8080/v1/media/transcribe" \
  -H "x-api-key: demo-test-api-key-123" \
  -H "Content-Type: application/json" \
  -d '{
    "media_url": "FILE_URL_HERE",
    "task": "transcribe",
    "include_text": true,
    "include_srt": true,
    "include_segments": true,
    "id": "test-transcribe"
  }'
```

---

## 📊 **Các tham số tùy chỉnh**

### **Cho Download API:**
```json
{
  "subtitles": {
    "download": true,
    "languages": ["en", "vi", "ja", "ko", "zh", "es", "fr"],
    "format": "srt",        // hoặc "vtt", "json3"
    "cloud_upload": true    // upload lên cloud storage
  },
  "audio": {
    "extract": true,
    "format": "mp3",        // hoặc "m4a", "wav"
    "quality": "best"
  },
  "format": {
    "quality": "best",      // hoặc "worst", "720p"
    "resolution": "720p"
  }
}
```

### **Cho Transcribe API:**
```json
{
  "task": "transcribe",           // hoặc "translate"
  "include_text": true,           // text thuần
  "include_srt": true,            // format SRT
  "include_segments": true,       // segments với timestamps
  "word_timestamps": true,        // timestamp cho từng từ
  "language": "en",               // ngôn ngữ nguồn
  "response_type": "direct"       // hoặc "cloud"
}
```

---

## 🎯 **Workflow hoàn chỉnh**

### **Bước 1: Kiểm tra video có subtitle không**
```bash
curl -X POST "http://localhost:8080/v1/BETA/media/download" \
  -d '{"media_url": "YOUTUBE_URL", "subtitles": {"download": true}}'
```

### **Bước 2A: Nếu có subtitle → Download trực tiếp**
```bash
# Kết quả sẽ có subtitle_url để download
```

### **Bước 2B: Nếu không có subtitle → Transcribe**
```bash
# 1. Download audio
curl -X POST "http://localhost:8080/v1/BETA/media/download" \
  -d '{"media_url": "YOUTUBE_URL", "audio": {"extract": true}}'

# 2. Transcribe audio
curl -X POST "http://localhost:8080/v1/media/transcribe" \
  -d '{"media_url": "AUDIO_URL", "include_srt": true}'
```

---

## 🐛 **Troubleshooting**

### **Lỗi thường gặp:**

1. **"Sign in to confirm you're not a bot"**
   - **Giải pháp**: Sử dụng cookies hoặc thử video khác

2. **"No cloud storage settings provided"**
   - **Giải pháp**: Đây chỉ là warning, API vẫn hoạt động

3. **"Invalid data found when processing input"**
   - **Giải pháp**: URL không phải direct link, cần download trước

4. **"404 Not Found"**
   - **Giải pháp**: Kiểm tra URL có accessible không

### **Tips tối ưu:**
- Sử dụng `webhook_url` cho video dài
- Set `cloud_upload: false` nếu muốn kết quả nhanh
- Chọn `languages` phù hợp với video
- Sử dụng `include_segments: true` để có timestamps chi tiết

---

## 📞 **Hỗ trợ**

Nếu gặp vấn đề, kiểm tra:
1. API key có đúng không
2. Server có đang chạy trên port 8080
3. URL video có accessible không
4. Format request có đúng JSON schema

**Happy transcribing! 🎉**