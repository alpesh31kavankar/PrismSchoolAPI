# app/api/teacher.py

import os
import shutil
import uuid
from fastapi import APIRouter, Form, File, UploadFile, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.teacher import Teacher

router = APIRouter(prefix="/teachers", tags=["Teachers"])

UPLOAD_DIR = "uploads/teachers"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
async def create_teacher(
    name: str = Form(...),
    subject: str = Form(...),
    rating: float = Form(...),
    profile_image: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    image_filename = None
    if profile_image:
        ext = profile_image.filename.split('.')[-1]
        image_filename = f"{uuid.uuid4().hex}.{ext}"
        image_path = os.path.join(UPLOAD_DIR, image_filename)
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(profile_image.file, buffer)

    teacher = Teacher(
        name=name,
        subject=subject,
        rating=rating,
        profile_image=image_filename
    )
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return {"message": "Teacher created", "data": teacher}

@router.get("/")
def get_teachers(db: Session = Depends(get_db)):
    return db.query(Teacher).all()

@router.delete("/{teacher_id}")
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")

    if teacher.profile_image:
        image_path = os.path.join(UPLOAD_DIR, teacher.profile_image)
        if os.path.exists(image_path):
            os.remove(image_path)

    db.delete(teacher)
    db.commit()
    return {"message": "Teacher deleted successfully"}

@router.put("/{teacher_id}")
async def update_teacher(
    teacher_id: int,
    name: str = Form(...),
    subject: str = Form(...),
    rating: float = Form(...),
    profile_image: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")

    teacher.name = name
    teacher.subject = subject
    teacher.rating = rating

    if profile_image:
        if teacher.profile_image:
            old_path = os.path.join(UPLOAD_DIR, teacher.profile_image)
            if os.path.exists(old_path):
                os.remove(old_path)

        ext = profile_image.filename.split('.')[-1]
        image_filename = f"{uuid.uuid4().hex}.{ext}"
        image_path = os.path.join(UPLOAD_DIR, image_filename)
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(profile_image.file, buffer)
        teacher.profile_image = image_filename

    db.commit()
    db.refresh(teacher)
    return {"message": "Teacher updated successfully", "data": teacher}
