from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import text
import os
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DB_URL")

engine = create_engine(db_url)

# every time you connect to something, it's session
session = sessionmaker(autoflush=False,autocommit=False,bind=engine)