import os
from dotenv import load_dotenv

load_dotenv()


# SECURITY
SECRET_KEY: str = os.getenv("SECRET_KEY")


# CLOUDINARY
CLOUDINARY_CLOUD_NAME: str = os.getenv("CLOUDINARY_CLOUD_NAME")
CLOUDINARY_API_KEY: str = os.getenv("CLOUDINARY_API_KEY")
CLOUDINARY_API_SECRET: str = os.getenv("CLOUDINARY_API_SECRET")


# DATABASE (PostgreSQL)
DATABASE_URL: str = os.getenv("DATABASE_URL")