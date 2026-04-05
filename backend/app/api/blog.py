from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.models.user import User
from app.models.blog import Blog
from app.schemas.blog import BlogCreate, BlogResponse
from app.core.db import get_session
from app.core.auth import get_current_user

router = APIRouter(prefix="/blogs", tags=["Blogs"])


# GET all
@router.get("/", response_model=list[BlogResponse])
def get_all(session: Session = Depends(get_session)):
    statement = select(Blog)
    blogs = session.exec(statement).all()
    return blogs


# GET by id
@router.get("/{id}", response_model=BlogResponse)
def get_by_id(id: int, session: Session = Depends(get_session)):
    blog = session.get(Blog, id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog


# POST
@router.post("/", response_model=BlogResponse, status_code=201)
def create(
    data: BlogCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    blog = Blog(title=data.title, content=data.content, user_id=current_user.id)  # type: ignore
    session.add(blog)
    session.commit()
    session.refresh(blog)
    return blog


# PUT
@router.put("/{id}", response_model=BlogResponse)
def update(
    id: int,
    data: BlogCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    blog = session.get(Blog, id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    # Cek kepemilikan
    if blog.user_id != current_user.id:  # type: ignore
        raise HTTPException(403, "Not authorized to update this blog")

    for key, value in data.model_dump().items():
        setattr(blog, key, value)

    session.add(blog)
    session.commit()
    session.refresh(blog)
    return blog


# DELETE
@router.delete("/{id}", status_code=204)
def delete(
    id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    blog = session.get(Blog, id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    # Cek kepemilikan
    if blog.user_id != current_user.id:  # type: ignore
        raise HTTPException(403, "Not authorized to delete this blog")

    session.delete(blog)
    session.commit()
    return None
