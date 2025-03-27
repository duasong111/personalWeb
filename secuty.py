# 登录安全配置

from typing import Optional, Tuple
from datetime import datetime, timedelta
import jwt
import bcrypt
from http import HTTPStatus

SECRET_KEY = "your-secret-key-here"  # 请使用安全的密钥，建议从环境变量读取
JWT_ALGORITHM = "HS256"
TOKEN_EXPIRATION = 30  # token 有效期（分钟）
def generate_jwt_token(user_id: str) -> str:
    """生成 JWT token"""
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION),
        "iat": datetime.utcnow()  # token 创建时间
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=JWT_ALGORITHM)
def verify_jwt_token(token: str) -> Optional[dict]:
    """验证 JWT token 并返回 payload"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # token 已过期
    except jwt.InvalidTokenError:
        return None  # token 无效