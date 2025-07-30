# 🎬 Bilibili Subtitle Downloader

Chương trình Python độc lập để tải subtitle từ video Bilibili sử dụng API có sẵn.

## ✨ Tính năng

- ✅ Tải subtitle cho nhiều ngôn ngữ
- ✅ Hỗ trợ các định dạng: SRT, VTT, JSON3, XML
- ✅ Tự động fallback sang định dạng có sẵn
- ✅ Lưu subtitle vào file local
- ✅ Hỗ trợ video private với cookie
- ✅ Thông tin chi tiết về video
- ✅ Giao diện command line dễ sử dụng

## 🚀 Cài đặt

### 1. Cài đặt dependencies

```bash
pip install requests
```

### 2. Cấu hình API

Chỉnh sửa file `bilibili_subtitle_downloader.py` hoặc sử dụng tham số:

```python
# Thay đổi các giá trị mặc định
--api-url "http://your-api-server.com"
--api-key "your_actual_api_key"
```

## 📋 Cách sử dụng

### 1. Sử dụng cơ bản

```bash
python bilibili_subtitle_downloader.py -u "https://www.bilibili.com/video/BV1xx411c7mu"
```

### 2. Chỉ định ngôn ngữ và định dạng

```bash
python bilibili_subtitle_downloader.py \
  -u "https://www.bilibili.com/video/BV1xx411c7mu" \
  -l zh-Hans en \
  -f srt
```

### 3. Tải danmaku (XML format)

```bash
python bilibili_subtitle_downloader.py \
  -u "https://www.bilibili.com/video/BV1xx411c7mu" \
  -f xml
```

### 4. Lưu vào thư mục local

```bash
python bilibili_subtitle_downloader.py \
  -u "https://www.bilibili.com/video/BV1xx411c7mu" \
  --save-local ./subtitles
```

### 5. Sử dụng với cookie (video private)

```bash
python bilibili_subtitle_downloader.py \
  -u "https://www.bilibili.com/video/BV1xx411c7mu" \
  --cookie "SESSDATA=abc123; bili_jct=def456"
```

### 6. Không upload lên cloud storage

```bash
python bilibili_subtitle_downloader.py \
  -u "https://www.bilibili.com/video/BV1xx411c7mu" \
  --no-cloud
```

## 📖 Tham số

| Tham số | Mô tả | Bắt buộc |
|---------|-------|----------|
| `-u, --url` | URL video Bilibili | ✅ |
| `-l, --languages` | Danh sách ngôn ngữ | ❌ |
| `-f, --format` | Định dạng subtitle | ❌ |
| `--no-cloud` | Không upload lên cloud | ❌ |
| `--cookie` | Cookie cho video private | ❌ |
| `--save-local` | Lưu vào thư mục local | ❌ |
| `--api-url` | URL API server | ❌ |
| `--api-key` | API key | ❌ |

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
| `danmaku` | Danmaku (弹幕) |

## 📝 Định dạng subtitle

| Định dạng | Mô tả | Hỗ trợ |
|-----------|-------|--------|
| `srt` | SubRip Subtitle | ✅ (nếu có) |
| `vtt` | Web Video Text Tracks | ✅ (nếu có) |
| `json3` | YouTube JSON format | ✅ (nếu có) |
| `xml` | Danmaku XML format | ✅ (mặc định) |

## 📤 Ví dụ output

```
🔄 Đang tải subtitle từ: https://www.bilibili.com/video/BV1xx411c7mu
📋 Tham số: {
  "media_url": "https://www.bilibili.com/video/BV1xx411c7mu",
  "subtitles": {
    "download": true,
    "format": "xml"
  },
  "cloud_upload": true
}
✅ Tải subtitle thành công!

==================================================
📊 TÓM TẮT KẾT QUẢ
==================================================
🎬 Video: 重磅！天文学家向全人类发出警告...
👤 Uploader: 灵犀档案
⏱️ Thời lượng: 947.598 giây
👁️ Lượt xem: 1832507

📝 Subtitle tìm thấy: 1
  🌍 danmaku:
    Định dạng: xml
    URL: https://cloud-storage-url/subtitle.xml
    Cloud URL: https://cloud-storage-url/subtitle.xml
==================================================

💾 Đang lưu subtitle vào: ./subtitles
📥 Đang tải subtitle danmaku...
✅ Đã lưu: ./subtitles/重磅！天文学家向全人类发出警告..._danmaku.xml
✅ Đã lưu 1 file subtitle
```

## 🔧 Sử dụng trong code Python

```python
from bilibili_subtitle_downloader import BilibiliSubtitleDownloader

# Khởi tạo downloader
downloader = BilibiliSubtitleDownloader(
    api_url="http://localhost:5000",
    api_key="your_api_key"
)

# Tải subtitle
result = downloader.download_subtitle(
    video_url="https://www.bilibili.com/video/BV1xx411c7mu",
    languages=["zh-Hans", "en"],
    format="srt"
)

# In kết quả
downloader.print_result_summary(result)

# Lưu vào file local
saved_files = downloader.save_subtitle_to_file(result, "./subtitles")
print(f"Đã lưu {len(saved_files)} file")
```

## 📝 Lưu ý

1. **API Server**: Cần có API server chạy với endpoint `/v1/BETA/media/download`
2. **Danmaku**: Nhiều video chỉ có danmaku (bullet comments), không có subtitle thực sự
3. **Fallback**: Nếu định dạng yêu cầu không có, sẽ sử dụng định dạng có sẵn
4. **Cookie**: Cần cookie hợp lệ cho video private
5. **Cloud Storage**: Subtitle sẽ được upload lên cloud storage nếu không dùng `--no-cloud`

## 🐛 Xử lý lỗi

### Lỗi kết nối
```bash
❌ Lỗi kết nối: Kiểm tra lại URL API và kết nối mạng
```
**Giải pháp**: Kiểm tra API server có đang chạy không

### Lỗi API
```bash
❌ Lỗi API: 401
Thông báo: Unauthorized
```
**Giải pháp**: Kiểm tra API key có đúng không

### Không có subtitle
```bash
❌ Không tìm thấy subtitle
```
**Giải pháp**: Video có thể không có subtitle, thử video khác

## 🔗 Liên kết

- [API Documentation](BILIBILI_SUBTITLE_GUIDE.md)
- [No-Code Architects Toolkit](README.md)

---

**Made with ❤️ for the Bilibili community**