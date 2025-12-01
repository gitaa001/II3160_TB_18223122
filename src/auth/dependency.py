from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from src.auth.auth import decode_access_token, get_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="]/token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_access_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    user = get_user(username)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    if user.get("disabled"):
        raise HTTPException(status_code=400, detail="Inactive user")
    return user
