# app/schemas/teacher.py

from pydantic import BaseModel
from typing import Optional

class TeacherBase(BaseModel):
    name: str
    subject: str
    rating: float

class TeacherCreate(TeacherBase):
    pass  # no image in JSON here

class TeacherOut(TeacherBase):
    id: int
    profile_image: Optional[str]  # image filename or URL

    class Config:
        orm_mode = True
