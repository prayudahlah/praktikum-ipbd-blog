from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.core.db import get_session
from app.core.auth import create_token, get_current_user
from app.models.user import User
from app.schemas.user import UserRegister, UserLogin, TokenResponse

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=TokenResponse, status_code=201)
def register(data: UserRegister, session: Session = Depends(get_session)):
    existing = session.exec(select(User).where(User.username == data.username)).first()
    if existing:
        raise HTTPException(400, "Username already exists")

    user = User(username=data.username)
    session.add(user)
    session.commit()
    session.refresh(user)

    return TokenResponse(access_token=create_token(user.id), user_id=user.id)  # type: ignore


@router.post("/login", response_model=TokenResponse)
def login(data: UserLogin, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.username == data.username)).first()

    if not user:
        raise HTTPException(401, "User not found")

    return TokenResponse(access_token=create_token(user.id), user_id=user.id)  # type: ignore


@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {"id": current_user.id, "username": current_user.username}
