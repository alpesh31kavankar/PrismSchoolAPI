# DATABASE_URL = "postgresql://postgres:2021Prismit$@localhost:5432/PrismSchoolDB"


# DATABASE_URL = "postgresql://prism:GyXzhosyeNZfI6ffPCXuHajXqoTLOJhe@dpg-d2i153be5dus73e8u17g-a.oregon-postgres.render.com:5432/prismschooldb"
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:2021Prismit$@localhost:5432/PrismSchoolDB"  # fallback for local
)
