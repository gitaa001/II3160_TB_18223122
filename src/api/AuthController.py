from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import timedelta
from src.auth.auth import authenticate_user, create_access_token, pwd_context, dummy_users_db
from src.auth.config import TOKEN_EXPIRE_MINUTES

router = APIRouter(tags=["Auth"])

# ============================
# REGISTER REQUEST MODEL
# ============================
class RegisterRequest(BaseModel):
    username: str
    full_name: str
    password: str


# ============================
# REGISTER 
# ============================
@router.post("/register")
def register(body: RegisterRequest):
    if body.username in dummy_users_db:
        raise HTTPException(status_code=400, detail="Username already exists")

    dummy_users_db[body.username] = {
        "username": body.username,
        "full_name": body.full_name,
        "password": body.password,
        "disabled": False,
    }

    return {"message": "User registered successfully"}


# ============================
# LOGIN 
# ============================
@router.post("/login")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(subject=user["username"], expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}
