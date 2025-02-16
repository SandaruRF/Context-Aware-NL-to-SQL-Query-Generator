import os
from dotenv import load_dotenv

load_dotenv(override=True)
DATABASE_URL = os.getenv("") #DATABASE_URL
if not DATABASE_URL:
    DATABASE_URL = "mysql+pymysql://root:200266@localhost/chinook"

#mysql+pymysql://root:200266@localhost/chinook
#postgresql://postgres:200266@localhost:5432/chinook
#Microsoft SQL Server
#MariaDB
#Oracle Database
#sqlite:///Chinook_Sqlite.sqlite
#Amazon Redshift