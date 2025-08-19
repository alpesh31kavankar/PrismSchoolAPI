from apscheduler.schedulers.background import BackgroundScheduler
from app.database import SessionLocal
from app.models.student import Student

top_students_cache = []
top_teachers_cache = []

def fetch_top_students():
    db = SessionLocal()
    try:
        top_students = db.query(Student).order_by(Student.cgpi.desc()).limit(3).all()
        global top_students_cache
        top_students_cache = [{"id": s.id, "name": s.name, "cgpi": s.cgpi} for s in top_students]
        print("Top 3 students updated.")
    finally:
        db.close()

        

def fetch_top_teachers():
    db = SessionLocal()
    try:
        top_teachers = db.query(Teacher).order_by(Teacher.rating.desc()).limit(3).all()
        global top_teachers_cache
        top_teachers_cache = [{"id": t.id, "name": t.name, "rating": t.rating} for t in top_teachers]
        print("Top 3 teachers updated.")
    finally:
        db.close()

def evaluate_teacher_ratings():
    print("Evaluating teacher ratings...")

def start_cron_jobs():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_top_students, 'interval', seconds=60)
    scheduler.add_job(fetch_top_teachers, 'interval', seconds=60)
    scheduler.start()
