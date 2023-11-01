from dotenv import load_dotenv
from pathlib import Path

from dotenv import dotenv_values
config = dotenv_values(".env") 

ROOT_DB_HOST = config["DB_HOST"]
ROOT_DB_USER = config["DB_USER"]
ROOT_DB_PASSWORD = config["DB_PW"]
ROOT_DB_PORT = config["DB_PORT"]
ROOT_DB = config["DB"]
ROOT_SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{ROOT_DB_USER}:{ROOT_DB_PASSWORD}@{ROOT_DB_HOST}:{ROOT_DB_PORT}/{ROOT_DB}'


DB_HOST = config["USER_DB_HOST"]
DB_USER = config["USER_DB_USER"]
DB_PASSWORD = config["USER_DB_PW"]
DB_PORT = config["USER_DB_PORT"]
DB_SCHEMA = config["USER_DB"]

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_SCHEMA}'