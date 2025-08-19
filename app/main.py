from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import student, teacher, aboutus
from app.cronjobs import start_cron_jobs
from fastapi.staticfiles import StaticFiles
from app.models.teacher import Teacher

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",              # for local Angular dev
        "https://test.elpisglobalservice.com" # your hosted Angular app
    ],
    allow_methods=["*"],
    allow_headers=["*"]
)



app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.include_router(student.router, prefix="/students", tags=["Students"])
app.include_router(teacher.router)
app.include_router(aboutus.router, prefix="/aboutus", tags=["About Us"])

start_cron_jobs()
