import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:200266@localhost:5432/EagleCartDB")  #, "postgresql://user:password@localhost/dbname"