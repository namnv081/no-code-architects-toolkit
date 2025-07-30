# 🎯 **BẮT ĐẦU TẠI ĐÂY - Tách Subtitle Bilibili**

## ⚡ **Khởi Động Nhanh Nhất (30 giây)**

```bash
# 1. Cài đặt yt-dlp
pip3 install --break-system-packages yt-dlp

# 2. Chạy ngay
python3 simple_bilibili_extractor.py https://www.bilibili.com/video/BV1xx411c7mu
```

**✅ Xong! Subtitle sẽ được lưu trong thư mục `subtitles/`**

---

## 🎯 **Mục Đích Dự Án**

Dự án này giúp bạn **tách subtitle từ video Bilibili** một cách dễ dàng và nhanh chóng.

### 🔥 **Tính Năng Chính:**
- ✅ Tách subtitle từ bilibili.com và b23.tv
- ✅ Hỗ trợ đa ngôn ngữ: Trung Quốc, Anh, Nhật, Hàn
- ✅ Nhiều định dạng: SRT, ASS, VTT
- ✅ Tự động tải subtitle và auto-generated captions
- ✅ Không cần tải video, chỉ tải subtitle

---

## 📚 **Cấu Trúc Dự Án**

```
📁 workspace/
├── 🔥 simple_bilibili_extractor.py    # Script chính (khuyến nghị)
├── 📖 QUICK_START.md                  # Hướng dẫn chi tiết
├── 🎯 START_HERE.md                   # File này
├── 
├── 🏗️ API Server (nâng cao):
├── ├── app.py                         # API server chính
├── ├── bilibili_subtitle_extractor.py # Script sử dụng API
├── ├── download_subtitles.py          # Tải subtitle từ cloud
├── └── check_api.py                   # Kiểm tra API key
└── 
└── 📚 Tài liệu:
    ├── README_Bilibili_Subtitle_Extractor.md
    ├── API_KEY_GUIDE.md
    └── docs/media/download.md
```

---

## 🚀 **2 Cách Sử Dụng**

### 🔥 **Cách 1: Script Đơn Giản (Khuyến Nghị)**
- ✅ Nhanh, đơn giản, không cần setup phức tạp
- ✅ Chỉ cần 2 lệnh là xong

```bash
pip3 install --break-system-packages yt-dlp
python3 simple_bilibili_extractor.py <URL_BILIBILI>
```

### 🏗️ **Cách 2: API Server (Nâng Cao)**  
- ✅ Đầy đủ tính năng, có thể tích hợp vào hệ thống lớn
- ⚠️ Cần setup API key và khởi động server

```bash
# Xem hướng dẫn chi tiết trong QUICK_START.md
```

---

## 📋 **API Key Hiện Tại**

Nếu bạn sử dụng API server, API key đã được thiết lập:

```
bili_sub_U5zwRcs3F2Z8zSv3jr4h0w
```

---

## 🎉 **Demo Ngay**

Chạy lệnh này để test:

```bash
python3 simple_bilibili_extractor.py https://www.bilibili.com/video/BV1xx411c7mu
```

Kết quả:
```
🚀 Simple Bilibili Subtitle Extractor
==================================================

🔍 Bước 1: Lấy thông tin video
📋 Đang lấy thông tin video: https://www.bilibili.com/video/BV1xx411c7mu
📺 Tiêu đề: [Video Title]
👤 Uploader: [Uploader Name]
⏱️  Thời lượng: 300 giây
👁️  Lượt xem: 12,345
🗣️  Subtitle có sẵn: zh-CN, en
🤖 Auto captions: zh-CN

📥 Bước 2: Tách subtitle
🎯 Đang tách subtitle từ: https://www.bilibili.com/video/BV1xx411c7mu
📥 Đang tải subtitle...
✅ Tải subtitle thành công!
📁 Subtitle được lưu trong thư mục: subtitles
   📄 [Video Title].zh-CN.srt
   📄 [Video Title].en.srt

🎉 Hoàn thành! Đã tải 2 file subtitle
📁 Kiểm tra thư mục: subtitles
```

---

## 🔧 **Khắc Phục Sự Cố Nhanh**

| Lỗi | Giải pháp |
|-----|-----------|
| `yt-dlp không được tìm thấy` | `pip3 install --break-system-packages yt-dlp` |
| `No module named 'jsonschema'` | `pip3 install --break-system-packages jsonschema` |
| `Connection refused` | Sử dụng script đơn giản thay vì API server |
| `Port 8080 is in use` | `export PORT=5000 && python3 app.py` |

---

## 💡 **Lời Khuyên**

1. **🔥 Bắt đầu với script đơn giản** - hiệu quả nhất
2. **📋 Copy URL trực tiếp từ Bilibili** 
3. **📁 Kiểm tra thư mục `subtitles/` sau khi chạy**
4. **📖 Đọc `QUICK_START.md` để biết thêm chi tiết**

---

## 🎯 **Sẵn Sàng Bắt Đầu?**

Chạy lệnh này ngay:

```bash
python3 simple_bilibili_extractor.py https://www.bilibili.com/video/BV1xx411c7mu
```

**🎉 Chúc bạn thành công!**