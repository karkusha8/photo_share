import cloudinary.uploader
import app.config.cloudinary


def upload_image(file):
    result = cloudinary.uploader.upload(file)

    return result["secure_url"], result["public_id"]


def generate_transformed_url(public_id: str):
    return cloudinary.CloudinaryImage(public_id).build_url(
        width=300,
        height=300,
        crop="fill"
    )