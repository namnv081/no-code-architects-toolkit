# Bilibili Subtitle Extractor

🎯 **Công cụ tách subtitle từ video Bilibili** sử dụng No-Code Architects Toolkit API

## 📋 Tổng quan

Bộ công cụ này giúp bạn dễ dàng tách và tải subtitle từ video Bilibili. Sử dụng `yt-dlp` và API mạnh mẽ để hỗ trợ nhiều định dạng subtitle và ngôn ngữ khác nhau.

## 🚀 Cài đặt

### 1. Khởi động API Server

Trước tiên, bạn cần khởi động API server:

```bash
# Cài đặt dependencies
pip install -r requirements.txt

# Khởi động server
python app.py
```

Server sẽ chạy tại `http://localhost:5000`

### 2. Lấy API Key

Bạn cần có API key để xác thực. Kiểm tra file `config.py` hoặc tài liệu API để biết cách lấy API key.

## 🛠️ Sử dụng

### Script 1: `bilibili_subtitle_extractor.py`

Tách subtitle từ video Bilibili và lưu thông tin vào file JSON.

#### Cú pháp:
```bash
python bilibili_subtitle_extractor.py <API_KEY> <BILIBILI_URL> [languages] [format]
```

#### Ví dụ:

```bash
# Tải tất cả subtitle có sẵn
python bilibili_subtitle_extractor.py your_api_key https://www.bilibili.com/video/BV1xx411c7mu

# Tải subtitle tiếng Trung và tiếng Anh
python bilibili_subtitle_extractor.py your_api_key https://www.bilibili.com/video/BV1xx411c7mu zh-CN,en

# Tải subtitle định dạng VTT
python bilibili_subtitle_extractor.py your_api_key https://www.bilibili.com/video/BV1xx411c7mu zh-CN vtt
```

#### Tham số:

- `API_KEY`: API key để xác thực
- `BILIBILI_URL`: URL video Bilibili
- `languages` (tùy chọn): Danh sách mã ngôn ngữ, cách nhau bởi dấu phẩy
- `format` (tùy chọn): Định dạng subtitle (`srt`, `vtt`, `json3`)

#### Mã ngôn ngữ phổ biến:

- `zh-CN`: Tiếng Trung giản thể
- `zh-TW`: Tiếng Trung phồn thể
- `en`: Tiếng Anh
- `ja`: Tiếng Nhật
- `ko`: Tiếng Hàn

### Script 2: `download_subtitles.py`

Tải subtitle từ kết quả JSON và lưu vào file local.

#### Cú pháp:
```bash
python download_subtitles.py <JSON_RESULT_FILE> [output_directory]
```

#### Ví dụ:

```bash
# Tải subtitle vào thư mục mặc định
python download_subtitles.py bilibili_subtitle_result_1234567890.json

# Tải subtitle vào thư mục tùy chỉnh
python download_subtitles.py bilibili_subtitle_result_1234567890.json my_subtitles
```

## 📁 Cấu trúc thư mục output

```
subtitles/
└── Tên_Video/
    ├── Tên_Video.zh-CN.srt
    ├── Tên_Video.en.srt
    └── Tên_Video.ja.srt
```

## 🔧 Quy trình hoàn chỉnh

### Bước 1: Tách subtitle
```bash
python bilibili_subtitle_extractor.py your_api_key https://www.bilibili.com/video/BV1xx411c7mu zh-CN,en
```

Kết quả: Tạo file `bilibili_subtitle_result_1234567890.json`

### Bước 2: Tải subtitle
```bash
python download_subtitles.py bilibili_subtitle_result_1234567890.json
```

Kết quả: Subtitle được lưu trong thư mục `subtitles/`

## 📊 Ví dụ kết quả

### Thông tin video được hiển thị:
```
📺 Thông tin video:
   Tiêu đề: 【官方MV】洛天依 言和《普通DISCO》
   Thời lượng: 226 giây
   Người tải lên: Luo Tianyi Official
   Lượt xem: 15234567

📄 Subtitle đã tải:
   🌐 Ngôn ngữ: zh-CN
      📎 URL: https://storage.example.com/subtitles/video_zh-CN.srt
      📋 Định dạng: srt

   🌐 Ngôn ngữ: en
      📎 URL: https://storage.example.com/subtitles/video_en.srt
      📋 Định dạng: srt
```

### Preview nội dung subtitle:
```
🌐 Đang tải subtitle zh-CN...
✅ Đã tải subtitle: subtitles/普通DISCO/普通DISCO.zh-CN.srt
   📄 Preview (156 từ):
      1
      00:00:01,000 --> 00:00:03,500
      欢迎来到普通disco

      2
      00:00:04,000 --> 00:00:06,500
      今夜我们一起跳舞
      ...
```

## ⚠️ Lưu ý quan trọng

1. **API Key**: Đảm bảo bạn có API key hợp lệ
2. **Server**: API server phải đang chạy
3. **URL Bilibili**: Chỉ hỗ trợ URL từ bilibili.com và b23.tv
4. **Subtitle**: Không phải tất cả video đều có subtitle
5. **Ngôn ngữ**: Một số ngôn ngữ có thể không có sẵn cho mọi video

## 🐛 Xử lý lỗi

### Lỗi thường gặp:

1. **"Invalid API key"**: Kiểm tra API key
2. **"URL không phải là URL Bilibili hợp lệ"**: Kiểm tra định dạng URL
3. **"Không tìm thấy subtitle nào"**: Video không có subtitle hoặc ngôn ngữ không có sẵn
4. **Connection error**: Kiểm tra kết nối mạng và API server

### Debug:

Kiểm tra file JSON kết quả để xem thông tin chi tiết về lỗi:
```bash
cat bilibili_subtitle_result_1234567890.json | jq .
```

## 🔧 Tùy chỉnh nâng cao

### Sử dụng webhook:

```python
from bilibili_subtitle_extractor import BilibiliSubtitleExtractor

extractor = BilibiliSubtitleExtractor("your_api_key")
result = extractor.extract_subtitles(
    bilibili_url="https://www.bilibili.com/video/BV1xx411c7mu",
    languages=["zh-CN", "en"],
    webhook_url="https://your-webhook-url.com/callback"
)
```

### Thay đổi API server:

```python
extractor = BilibiliSubtitleExtractor(
    api_key="your_api_key",
    base_url="https://your-api-server.com"
)
```

## 📞 Hỗ trợ

Nếu gặp vấn đề, hãy kiểm tra:
1. Log của API server
2. File JSON kết quả để xem thông tin lỗi
3. Kết nối mạng và quyền truy cập Bilibili

---

🎉 **Chúc bạn sử dụng công cụ thành công!**