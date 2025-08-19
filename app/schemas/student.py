from pydantic import BaseModel
from datetime import datetime

class StudentOut(BaseModel):
    id: int
    name: str
    cgpi: float
    created_at: datetime

    class Config:
        orm_mode = True


class StudentCreate(BaseModel):
    name: str
    cgpi: float
