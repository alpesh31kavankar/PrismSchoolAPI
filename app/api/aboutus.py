from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_aboutus():
    return {"message": "About Us Page"}
