from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.dependencies import get_db
from app.models.photo import Photo
from app.schemas.photo import PhotoResponse, PhotoUpdate
from app.services.cloudinary import upload_image
from app.services.photo import create_photo, get_photos

router = APIRouter(prefix="/photos", tags=["photos"])


@router.post("/", response_model=PhotoResponse)
def create_photo_route(
    file: UploadFile = File(...),
    description: str = "",
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Only JPG or PNG images allowed")


    MAX_SIZE = 5 * 1024 * 1024
    contents = file.file.read()

    if len(contents) > MAX_SIZE:
        raise HTTPException(status_code=400, detail="File too large (max 5MB)")

    file.file.seek(0)

    image_url, public_id = upload_image(file.file)

    return create_photo(
        db,
        user.id,
        image_url,
        public_id,
        description,
        []
    )


@router.get("/", response_model=list[PhotoResponse])
def get_photos_route(
    search: str | None = None,
    tag: str | None = None,
    sort: str | None = None,
    db: Session = Depends(get_db)
):
    return get_photos(db, search, tag, sort)


@router.delete("/{photo_id}")
def delete_photo_route(
    photo_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    photo = db.query(Photo).filter(Photo.id == photo_id).first()

    if not photo:
        raise HTTPException(status_code=404, detail="Photo not found")

    if photo.owner_id != user.id and user.role != "admin":
        raise HTTPException(status_code=403, detail="Not allowed")

    db.delete(photo)
    db.commit()

    return {"message": "Photo deleted"}


@router.put("/{photo_id}", response_model=PhotoResponse)
def update_photo_route(
    photo_id: int,
    data: PhotoUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    photo = db.query(Photo).filter(Photo.id == photo_id).first()

    if not photo:
        raise HTTPException(status_code=404, detail="Photo not found")

    if photo.owner_id != user.id:
        raise HTTPException(status_code=403, detail="Not allowed")

    photo.description = data.description
    db.commit()
    db.refresh(photo)

    return photo