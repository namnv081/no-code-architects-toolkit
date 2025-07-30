# 🚀 **CÁCH KHỞI ĐỘNG DỰ ÁN - Tách Subtitle/Danmaku Bilibili**

## ❌ **VẤN ĐỀ BẠN GẶP PHẢI**

Lỗi: `ValueError: API_KEY environment variable is not set`

## ✅ **GIẢI PHÁP HOÀN CHỈNH**

### **Bước 1: Thiết lập API Key**

```bash
# Thiết lập API key cho session hiện tại
export API_KEY=bili_sub_U5zwRcs3F2Z8zSv3jr4h0w

# Tạo file .env để lưu vĩnh viễn
echo "API_KEY=bili_sub_U5zwRcs3F2Z8zSv3jr4h0w" > .env

# Thêm vào bashrc để tự động load
echo "export API_KEY=bili_sub_U5zwRcs3F2Z8zSv3jr4h0w" >> ~/.bashrc
```

### **Bước 2: Cài đặt Dependencies**

```bash
# Cài đặt packages cần thiết (với flag đặc biệt cho môi trường này)
pip3 install --break-system-packages -r requirements.txt
pip3 install --break-system-packages jsonschema yt-dlp
```

### **Bước 3: Khởi động Server (Tùy chọn)**

```bash
# Khởi động API server trong background
export API_KEY=bili_sub_U5zwRcs3F2Z8zSv3jr4h0w && python3 app.py &

# Kiểm tra server đã chạy chưa
curl http://localhost:8080/health
```

---

## 🔥 **CÁCH SỬ DỤNG NHANH NHẤT**

### **Tách Danmaku từ Bilibili (Không cần server)**

```bash
# Chạy script đơn giản để tách danmaku
python3 bilibili_danmaku_extractor.py https://www.bilibili.com/video/BV1xx411c7mu

# Hoặc chỉ xem có subtitle gì
python3 bilibili_danmaku_extractor.py --list https://www.bilibili.com/video/BV1xx411c7mu
```

### **Kết quả:**
- File danmaku XML sẽ được lưu trong thư mục `danmaku_output/`
- Chứa tất cả comment của người xem với timestamp

---

## 📁 **CẤU TRÚC PROJECT**

```
workspace/
├── 🔥 bilibili_danmaku_extractor.py    # Script tách danmaku (chính)
├── 🎯 simple_bilibili_extractor.py     # Script tách subtitle đơn giản  
├── 📖 HOW_TO_START_PROJECT.md          # File này
├── 🔑 .env                             # File chứa API key
├── 🏗️ app.py                          # API server (phức tạp hơn)
└── 📁 danmaku_output/                  # Thư mục chứa kết quả
    └── 最终鬼畜蓝蓝路.danmaku.xml       # File danmaku đã tải
```

---

## 🎯 **THÔNG TIN QUAN TRỌNG**

### **API Key hiện tại:**
```
bili_sub_U5zwRcs3F2Z8zSv3jr4h0w
```

### **Bilibili hỗ trợ:**
- ✅ **Danmaku**: Comment overlay (có sẵn)
- ❌ **Subtitle thông thường**: Thường không có hoặc ít
- ✅ **Auto-generated**: Một số video có

### **URL được hỗ trợ:**
- `https://www.bilibili.com/video/BV***`
- `https://b23.tv/***`

---

## 🛠️ **TROUBLESHOOTING**

### **1. Lỗi API_KEY:**
```bash
export API_KEY=bili_sub_U5zwRcs3F2Z8zSv3jr4h0w
```

### **2. Lỗi module không tìm thấy:**
```bash
pip3 install --break-system-packages yt-dlp
```

### **3. Server không chạy được:**
Sử dụng script đơn giản thay thế:
```bash
python3 bilibili_danmaku_extractor.py <URL>
```

---

## 🎉 **DEMO THÀNH CÔNG**

Đã test thành công với video: `https://www.bilibili.com/video/BV1xx411c7mu`

File kết quả: `danmaku_output/最终鬼畜蓝蓝路.danmaku.xml` (120KB)

Chứa hàng nghìn comment với format:
```xml
<d p="thời_gian,loại,kích_thước,màu,timestamp,pool,hash,id,level">nội dung comment</d>
```

**✅ DỰ ÁN ĐÃ SẴN SÀNG SỬ DỤNG!**