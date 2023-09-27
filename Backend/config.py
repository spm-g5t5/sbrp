from dotenv import load_dotenv
load_dotenv()

import os
TESTING = "TEST"
DB_HOST = os.getenv("HOST")
DB_USER = os.getenv("USER")
DB_PASSWORD = os.getenv("PASSWORD")
DB_SCHEMA = os.getenv("DB")