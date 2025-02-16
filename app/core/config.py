import os
from dotenv import load_dotenv

load_dotenv(override=True)
DATABASE_URL = os.getenv("") #DATABASE_URL
if not DATABASE_URL:
    DATABASE_URL = "mysql+pymysql://root:200266@localhost/chinook"
