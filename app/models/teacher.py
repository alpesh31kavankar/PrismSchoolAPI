from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    rating = Column(Float, nullable=False)
    profile_image = Column(String, nullable=True) 
