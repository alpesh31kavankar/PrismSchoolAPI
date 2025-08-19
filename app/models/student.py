from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database import Base

class Student(Base):
    __tablename__ = "students"  # Table name in PostgreSQL

    id = Column(Integer, primary_key=True, index=True)   # Auto-increment primary key
    name = Column(String, nullable=False)                # Student name
    cgpi = Column(Float, nullable=False)                 # CGPI score
    created_at = Column(DateTime, default=datetime.utcnow)  # Timestamp of creation
