from sqlalchemy.orm import Session
from app.models.transform import Transform
from app.utils.qr import generate_qr
from app.services.cloudinary import generate_transformed_url


def create_transform(db: Session, photo):
    transform_url = generate_transformed_url(photo.public_id)

    qr_path = generate_qr(transform_url, f"photo_{photo.id}")

    transform = Transform(
        photo_id=photo.id,
        transform_url=transform_url,
        qr_code=qr_path
    )

    db.add(transform)
    db.commit()
    db.refresh(transform)

    return transform