from sqlalchemy import Column, Integer, Text
from app.database import Base

class AboutUs(Base):
    __tablename__ = "aboutus"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
