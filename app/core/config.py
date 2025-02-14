import os
from dotenv import load_dotenv

load_dotenv(override=True)
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    DATABASE_URL = "postgresql://postgres:200266@localhost:5432/EagleCartDB"
    
print(f"DATABASE_URL: {DATABASE_URL}")