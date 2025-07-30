# 🚀 Hướng dẫn chạy No-Code Architects Toolkit API

## 📖 Giới thiệu
**No-Code Architects Toolkit API** là một API miễn phí 100% được xây dựng bằng Python Flask, chuyên xử lý các loại media khác nhau như:
- Chuyển đổi audio/video
- Transcription (chuyển âm thanh thành văn bản)
- Translation (dịch thuật)
- Thêm caption cho video
- Quản lý files trên cloud services (Google Drive, Amazon S3, GCS, Dropbox)

## 🛠️ Cách chạy dự án

### **Phương pháp 1: Chạy trực tiếp với Python (Khuyến nghị cho development)**

#### Bước 1: Cài đặt dependencies hệ thống
```bash
sudo apt update && sudo apt install -y python3-venv python3-full ffmpeg jq
```

#### Bước 2: Tạo virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Bước 3: Cài đặt Python dependencies
```bash
pip install -r requirements.txt
pip install jsonschema  # dependency bổ sung
```

#### Bước 4: Cấu hình môi trường
File `.env_variables.json` đã được tạo với cấu hình mặc định:
```json
{
  "API_KEY": "demo-test-api-key-123",
  "LOCAL_STORAGE_PATH": "/tmp",
  "MAX_QUEUE_LENGTH": "10",
  "GUNICORN_WORKERS": "4", 
  "GUNICORN_TIMEOUT": "300"
}
```

#### Bước 5: Chạy ứng dụng
```bash
# Kích hoạt virtual environment
source venv/bin/activate

# Thiết lập API key
export API_KEY="demo-test-api-key-123"

# Chạy với gunicorn (production-ready)
gunicorn --bind 0.0.0.0:8080 --workers 2 --timeout 300 app:app

# Hoặc chạy development server (Flask debug)
python3 app.py
```

#### Bước 6: Kiểm tra ứng dụng
```bash
# Test API endpoint
curl -X GET "http://localhost:8080/v1/toolkit/test" -H "x-api-key: demo-test-api-key-123"

# Nếu thành công, bạn sẽ nhận được response JSON
```

---

### **Phương pháp 2: Chạy với Docker**

#### Build Docker image
```bash
docker build -t no-code-architects-toolkit .
```

#### Chạy container
```bash
docker run -d -p 8080:8080 \
  -e API_KEY=demo-test-api-key-123 \
  -e LOCAL_STORAGE_PATH=/tmp \
  -e MAX_QUEUE_LENGTH=10 \
  -e GUNICORN_WORKERS=4 \
  -e GUNICORN_TIMEOUT=300 \
  no-code-architects-toolkit
```

#### Sử dụng script tự động (local.sh)
```bash
# Cấu hình variables trong .env_variables.json trước
chmod +x local.sh
./local.sh
```

---

## 🔧 Cấu hình nâng cao

### Variables môi trường quan trọng

#### **Bắt buộc**
- `API_KEY`: Key để xác thực API (VD: "demo-test-api-key-123")

#### **Storage (tùy chọn)**
- `LOCAL_STORAGE_PATH`: Đường dẫn lưu trữ tạm thời (mặc định: /tmp)

#### **S3-Compatible Storage (nếu sử dụng)**
```bash
S3_ENDPOINT_URL=https://nyc3.digitaloceanspaces.com
S3_ACCESS_KEY=your_access_key
S3_SECRET_KEY=your_secret_key  
S3_BUCKET_NAME=your_bucket_name
S3_REGION=nyc3
```

#### **Google Cloud Storage (nếu sử dụng)**
```bash
GCP_SA_CREDENTIALS='{"your":"service_account_json"}'
GCP_BUCKET_NAME=your_gcs_bucket_name
```

#### **Performance Tuning**
- `MAX_QUEUE_LENGTH`: Giới hạn số tasks đồng thời (mặc định: 0 = unlimited)
- `GUNICORN_WORKERS`: Số worker processes (mặc định: số CPU cores + 1)
- `GUNICORN_TIMEOUT`: Timeout cho worker (mặc định: 30s, khuyến nghị: 300-600s cho media files lớn)

---

## 🧪 Test API

### Endpoint test cơ bản
```bash
curl -X GET "http://localhost:8080/v1/toolkit/test" \
  -H "x-api-key: demo-test-api-key-123"
```

### Một số endpoints hữu ích khác:
- `/v1/media/transcribe` - Chuyển audio thành text
- `/v1/video/caption` - Thêm subtitle cho video
- `/v1/media/convert` - Chuyển đổi format media
- `/v1/image/screenshot/webpage` - Chụp screenshot trang web

---

## 📚 Tài liệu API

- **[README chính](README.md)** - Thông tin chi tiết về tất cả endpoints
- **[Postman Template](https://bit.ly/49Gkh61)** - Collection để test API
- **[NCA Toolkit API GPT](https://bit.ly/4feDDk4)** - AI assistant cho API

---

## 🐛 Troubleshooting

### Lỗi thường gặp:

1. **"ModuleNotFoundError"** 
   ```bash
   pip install [tên_module_bị_thiếu]
   ```

2. **"No cloud storage settings provided"**
   - Đây là warning bình thường nếu không cấu hình cloud storage
   - API vẫn hoạt động với local storage

3. **"Connection refused"**
   - Kiểm tra server có đang chạy không
   - Đảm bảo port 8080 không bị chặn

4. **"Permission denied"**
   ```bash
   chmod +x local.sh
   sudo chown -R $USER:$USER /tmp
   ```

---

## 📞 Hỗ trợ

- **Community**: [No-Code Architects Community](https://www.skool.com/no-code-architects)
- **Documentation**: Thư mục `docs/` trong dự án
- **Issues**: GitHub Issues của dự án

---

*Chúc bạn sử dụng API thành công! 🎉*