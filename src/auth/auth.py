from datetime import datetime, timedelta
from typing import Optional
from src.auth.config import SECRET_KEY, JWT_ALGORITHM, TOKEN_EXPIRE_MINUTES
from passlib.context import CryptContext
from jose import jwt 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  # GANTI ke argon2

dummy_users_db = {
    "user1": {
        "username": "user1",
        "full_name": "Demo User 1",
        "password": "secret1",
        "disabled": False,
    },
    "user2": {
        "username": "user2",
        "full_name": "Demo User 2",
        "password": "secret2",
        "disabled": False,
    },
}

# utils
def verify_password(plain_password: str, stored: str) -> bool:
    # cek apakah stored adalah hash (dimulai dengan $) atau plain password
    if isinstance(stored, str) and stored.startswith("$"):
        return pwd_context.verify(plain_password, stored)
    return plain_password == stored

def get_user(username: str) -> Optional[dict]:
    return dummy_users_db.get(username)

def authenticate_user(username: str, password: str) -> Optional[dict]:
    user = get_user(username)
    if not user:
        return None
    # PERBAIKI: cari hashed_password atau password
    stored = user.get("hashed_password") or user.get("password")
    if not stored or not verify_password(password, stored):
        return None
    return user

def create_access_token(subject: str, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = {"sub": subject}
    now = datetime.utcnow()
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "iat": now})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> dict:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
    return payload