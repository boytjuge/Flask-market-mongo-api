"# Flask-market-mongo-api" 

# 🛡️ Flask + MongoDB + JWT Authentication

ระบบตัวอย่างสำหรับการสร้าง Web API ด้วย Python Flask, MongoDB และ JWT (Access/Refresh Token) พร้อมระบบ Login, Logout, Refresh Token, Revoke Token (Blacklist).

---

## 📦 Features

- 🌐 แยกเส้นทาง Web (`/market/web`) และ API (`/market/api`)
- 🔒 Authentication ด้วย JWT Bearer Token
- 🔄 Refresh Token รองรับหมดอายุและการต่ออายุ Token
- 🚪 Logout พร้อม Revoke Refresh Token
- 🗂️ MongoDB สำหรับเก็บข้อมูล User และ Token
- 🔥 Config Token หมดอายุได้ (Access: 15 นาที, Refresh: 7 วัน)

---

## 📋 Project Structure

```plaintext
app/
  ├── __init__.py        # Initialize Flask app and extensions
  ├── config.py          # Config (Secret key, Mongo URI, JWT settings)
  ├── models/
  │    └── user_model.py  # MongoDB User & Login models
  ├── routes/
  │    ├── web.py        # Web routes (หน้าเว็บ)
  │    └── api.py        # API routes (Login, Logout, Refresh Token)
README.md
requirements.txt
```

---

## 🚀 Installation

1. Clone repository
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. สร้าง virtual environment (แนะนำ)
   ```bash
   python -m venv venv
   source venv/bin/activate    # หรือ venv\Scripts\activate สำหรับ Windows
   ```

3. ติดตั้ง dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. ตั้งค่า MongoDB (local หรือ cloud)  
   และแก้ไขค่า `MONGO_URI` ใน `app/config.py`

5. รันโปรเจกต์
   ```bash
   flask run --host=0.0.0.0 --port=6000
   ```

---

## 🛠️ API Endpoints

| Method | URL | Description | Auth |
|:-------|:----|:------------|:-----|
| POST | `/market/api/login` | เข้าสู่ระบบ | ❌ |
| POST | `/market/api/logout` | ออกจากระบบ (revoke refresh token) | 🔒 Refresh Token |
| POST | `/market/api/refresh` | ต่ออายุ Access Token | 🔒 Refresh Token |
| GET | `/market/api/protected` | ตัวอย่าง protected API | 🔒 Access Token |

> 📝 หมายเหตุ: 
> - Access Token ใช้สำหรับ API ปกติ
> - Refresh Token ใช้เฉพาะ `/refresh` และ `/logout`

---

## 🔑 Example (Token Usage)

1. Login เพื่อรับ Access Token และ Refresh Token

2. เรียก API ปกติ:
   ```http
   GET /market/api/protected
   Authorization: Bearer <access_token>
   ```

3. ต่ออายุ Access Token:
   ```http
   POST /market/api/refresh
   Authorization: Bearer <refresh_token>
   ```

4. ออกจากระบบ (Revoke):
   ```http
   POST /market/api/logout
   Authorization: Bearer <refresh_token>
   ```

---

## 📚 Tech Stack

- Python 3.11+
- Flask
- Flask-JWT-Extended
- PyMongo
- MongoDB
- JWT Standard (RFC7519)

---

## ✨ Future Improvements (Optional)

- เก็บ Blacklist Token ใน MongoDB หรือ Redis
- Refresh Token Rotation
- Multi-device Login Management
- Role-Based Access Control (RBAC)

---

## 📜 License

MIT License

---

> Developed with ❤️ by [your name]
