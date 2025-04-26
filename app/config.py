class Config:
    MONGO_URI = 'mongodb://localhost:27017/mydatabase'
    SECRET_KEY = 'your-secret-key'
    JWT_SECRET_KEY = 'your-jwt-secret-key' 
    
    # กำหนดอายุของ Token
    JWT_ACCESS_TOKEN_EXPIRES = 900       # 900 วินาที = 15 นาที
    JWT_REFRESH_TOKEN_EXPIRES = 604800    # 604800 วินาที = 7 วัน
    JWT_TOKEN_LOCATION = ['headers']
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['refresh'] 