from dotenv import load_dotenv
load_dotenv()

import os
TESTING = "TEST"
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PW")
DB_PORT = os.getenv("DB_PORT")
DB_SCHEMA = os.getenv("DB")

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_SCHEMA}"
