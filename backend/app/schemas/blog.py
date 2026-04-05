from sqlmodel import SQLModel


class BlogBase(SQLModel):
    title: str
    content: str


class BlogCreate(BlogBase):
    pass


class BlogResponse(BlogBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
