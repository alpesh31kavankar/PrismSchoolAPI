# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from app.database import SessionLocal
# from app.models import student as models
# from app.schemas import student as schemas

# router = APIRouter()

# # Dependency to get DB session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.get("/", response_model=list[schemas.StudentOut])
# def get_students(db: Session = Depends(get_db)):
#     students = db.query(models.Student).all()
#     return students

# @router.get("/top", response_model=list[schemas.StudentOut])
# def get_top_students(db: Session = Depends(get_db)):
#     # Example: get top 3 students by CGPI, descending order
#     top_students = db.query(models.Student).order_by(models.Student.cgpi.desc()).limit(3).all()
#     return top_students


# app/api/student.py


from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentOut

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET all students
@router.get("/", response_model=list[StudentOut])
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

# GET one student
@router.get("/{student_id}", response_model=StudentOut)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# POST new student
@router.post("/", response_model=StudentOut)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, cgpi=student.cgpi)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# PUT update student
@router.put("/{student_id}", response_model=StudentOut)
def update_student(student_id: int, student: StudentCreate, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    db_student.name = student.name
    db_student.cgpi = student.cgpi
    db.commit()
    db.refresh(db_student)
    return db_student

# DELETE student
@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": "Student deleted"}
