from sqlmodel import SQLModel


class UserRegister(SQLModel):
    username: str


class UserLogin(SQLModel):
    username: str


class TokenResponse(SQLModel):
    access_token: str
    type: str = "bearer"
    user_id: int
