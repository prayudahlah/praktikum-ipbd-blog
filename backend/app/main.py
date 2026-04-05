from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.db import create_db_and_tables
from app.models.user import User
from app.models.blog import Blog

from app.api import auth
from app.api import blog
from app.api import health


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating database tables...")
    create_db_and_tables()
    print("Database ready!")

    yield

    print("Shutting down...")


app = FastAPI(lifespan=lifespan)


app.include_router(auth.router, prefix="/api")
app.include_router(blog.router, prefix="/api")

app.include_router(health.router)
