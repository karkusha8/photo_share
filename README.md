# PhotoShare API

PhotoShare API is a backend service for uploading, managing, and processing images. It provides authentication, role-based access, tagging, comments, ratings, and image transformation features.

---

## Features

* JWT-based authentication
* Role-based access control (user, admin)
* Image upload via Cloudinary
* Photo tagging system
* Comments and ratings
* Image transformation support
* QR code generation for sharing
* RESTful API built with FastAPI
* PostgreSQL database
* Alembic migrations
* Test coverage ~90%

---

## Tech Stack

* Backend: FastAPI
* Database: PostgreSQL
* ORM: SQLAlchemy
* Migrations: Alembic
* Authentication: JWT
* Storage: Cloudinary
* Testing: Pytest
* Containerization: Docker

---

## Installation (Local)

Clone the repository:

```bash
git clone https://github.com/your-username/photo-share.git
cd photo-share
```

Create environment file:

```bash
cp .env.example .env
```

Edit `.env` and fill in your credentials.

Install dependencies:

```bash
poetry install
```

Run database migrations:

```bash
alembic upgrade head
```

Start the server:

```bash
uvicorn app.main:app --reload
```

Open API documentation:

```
http://localhost:8000/docs
```

---

## Docker Setup

Build and run containers:

```bash
docker-compose up --build
```

Apply migrations inside container:

```bash
docker exec -it photo_api alembic upgrade head
```

Open API documentation:

```
http://localhost:8000/docs
```

---

## Environment Variables

Create `.env` file based on `.env.example`:

```
DATABASE_URL=postgresql://postgres:postgres@db:5432/photo_db

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

CLOUD_NAME=your_cloud_name
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

## Testing

Run tests with coverage:

```bash
PYTHONPATH=. pytest --cov=app --cov-report=term-missing
```

---

## Project Structure

```
app/
 ├── auth/
 ├── config/
 ├── database/
 ├── models/
 ├── routes/
 ├── schemas/
 ├── services/
 ├── utils/
 └── main.py

tests/
alembic/
```

---

## Security Notes

* The `.env` file is not included in the repository
* Sensitive data such as API keys and secrets must be stored locally
* Use `.env.example` as a template

---

## Notes

* External services such as Cloudinary are mocked in tests
* The database is reset between test runs
* The project follows production-oriented structure and practices

---

## Author

karkusha8

---

## Deployment

The project is deployed on Render and is accessible at:

https://photo-share-skp2.onrender.com

Interactive API documentation (Swagger UI):

https://photo-share-skp2.onrender.com/docs

The application runs in a Docker container and uses PostgreSQL as the database.
## License

MIT
