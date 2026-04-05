from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .user import User


class Blog(SQLModel, table=True):
    __tablename__ = "blogs"  # type: ignore

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=200)
    content: str
    user_id: int = Field(foreign_key="users.id")

    user: "User" = Relationship(back_populates="blogs")
