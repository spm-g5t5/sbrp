from dotenv import load_dotenv
load_dotenv()
import os

ROOT_DB_HOST = os.getenv("DB_HOST")
ROOT_DB_USER = os.getenv("DB_USER")
ROOT_DB_PASSWORD = os.getenv("DB_PW")
ROOT_DB_PORT = os.getenv("DB_PORT")
ROOT_DB = os.getenv("DB")
ROOT_SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{ROOT_DB_USER}:{ROOT_DB_PASSWORD}@{ROOT_DB_HOST}:{ROOT_DB_PORT}/{ROOT_DB}'


DB_HOST = os.getenv("USER_DB_HOST")
DB_USER = os.getenv("USER_DB_USER")
DB_PASSWORD = os.getenv("USER_DB_PW")
DB_PORT = os.getenv("USER_DB_PORT")
DB_SCHEMA = os.getenv("USER_DB")

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_SCHEMA}'