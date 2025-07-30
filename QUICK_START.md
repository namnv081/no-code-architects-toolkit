# 🚀 Hướng Dẫn Khởi Động Nhanh - Tách Subtitle Bilibili

## 📋 Tóm Tắt
Dự án này cung cấp **2 cách** để tách subtitle từ video Bilibili:

1. **🔥 Cách Nhanh**: Sử dụng script đơn giản (khuyến nghị)  
2. **🏗️ Cách Đầy Đủ**: Sử dụng API server (phức tạp hơn)

---

## 🔥 **CÁCH 1: Script Đơn Giản (Khuyến Nghị)**

### Bước 1: Cài đặt yt-dlp
```bash
pip3 install --break-system-packages yt-dlp
```

### Bước 2: Chạy script
```bash
python3 simple_bilibili_extractor.py https://www.bilibili.com/video/BV1xx411c7mu
```

### ✅ **Xong!** 
Subtitle sẽ được lưu trong thư mục `subtitles/`

---

## 🏗️ **CÁCH 2: API Server (Nâng Cao)**

### Bước 1: Cài đặt dependencies
```bash
pip3 install --break-system-packages -r requirements.txt
pip3 install --break-system-packages jsonschema
```

### Bước 2: Thiết lập API key
```bash
export API_KEY=bili_sub_U5zwRcs3F2Z8zSv3jr4h0w
```

### Bước 3: Khởi động server
```bash
export PORT=5000
python3 app.py
```

### Bước 4: Sử dụng API
```bash
python3 bilibili_subtitle_extractor.py bili_sub_U5zwRcs3F2Z8zSv3jr4h0w https://www.bilibili.com/video/BV1xx411c7mu
```

---

## 🎯 **Các URL Bilibili Được Hỗ Trợ**

✅ **Hoạt động với:**
- `https://www.bilibili.com/video/BV1xx411c7mu`
- `https://b23.tv/abc123` (link rút gọn)
- `https://www.bilibili.com/video/av12345`

---

## 📁 **Kết Quả**

Sau khi chạy thành công, bạn sẽ có:

```
subtitles/
├── [Tên Video].zh-CN.srt    # Subtitle tiếng Trung giản thể
├── [Tên Video].zh-TW.srt    # Subtitle tiếng Trung phồn thể  
├── [Tên Video].en.srt       # Subtitle tiếng Anh (nếu có)
└── [Tên Video].ja.srt       # Subtitle tiếng Nhật (nếu có)
```

---

## 🔧 **Khắc Phục Sự Cố**

### ❌ Lỗi: "yt-dlp không được tìm thấy"
```bash
pip3 install --break-system-packages yt-dlp
```

### ❌ Lỗi: "No module named 'jsonschema'"
```bash
pip3 install --break-system-packages jsonschema
```

### ❌ Lỗi: "Port 8080 is in use"
```bash
export PORT=5000
python3 app.py
```

### ❌ Lỗi: "Connection refused"
Server chưa khởi động hoặc đang lỗi. Sử dụng **Cách 1** thay thế.

---

## 🎉 **Demo Nhanh**

Chạy lệnh này để test ngay:

```bash
python3 simple_bilibili_extractor.py https://www.bilibili.com/video/BV1xx411c7mu
```

Kết quả sẽ hiển thị:
- ✅ Thông tin video
- ✅ Danh sách subtitle có sẵn  
- ✅ File subtitle đã tải về

---

## 💡 **Lời Khuyên**

1. **Bắt đầu với Cách 1** - đơn giản và hiệu quả
2. **Sử dụng Cách 2** nếu cần tích hợp vào hệ thống lớn hơn
3. **Kiểm tra thư mục `subtitles/`** sau khi chạy
4. **Copy URL trực tiếp từ Bilibili** để đảm bảo chính xác

---

**🎯 Mục tiêu**: Giúp bạn tách subtitle từ Bilibili một cách nhanh chóng và dễ dàng!