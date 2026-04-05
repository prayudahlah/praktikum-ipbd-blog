# Praktikum IPBD Blog API
<p align="center">
  Prayuda Afifan Handoyo<br>
  L0224008 | Kelas A<br>
  Infrastruktur dan Platform Big Data
</p>

---

REST API sederhana untuk platform blog dengan autentikasi JWT.

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL 17
- **ORM**: SQLModel
- **Auth**: JWT (python-jose)
- **Package Manager**: UV

## Fitur

- Registrasi & Login (JWT)
- CRUD Blog Posts
- Authorization (hanya pemilik bisa edit/delete)

## Quick Start

```bash
# Clone repository
git clone https://github.com/prayudahlah/praktikum-ipbd-blog 
cd praktikum-ipbd-blog
```

```bash
# Start dengan Docker Compose
cd backend
uv sync
cd ..
docker compose up -d --build

# Atau untuk development
cd backend
uv sync
cd ..
docker compose up --watch --build
```

## API Documentation

```
Swagger UI: http://localhost:8000/docs
```

## API Endpoints

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| POST | `/api/auth/register` | Registrasi user |
| POST | `/api/auth/login` | Login user |
| GET | `/api/auth/me` | Get user info |
| GET | `/api/blogs/` | Get all blog |
| GET | `/api/blogs/{id}` | Get blog by id |
| POST | `/api/blogs/` | Create blog (auth) |
| PUT | `/api/blogs/{id}` | Update blog (auth) |
| DELETE | `/api/blogs/{id}` | Delete blog (auth) |
