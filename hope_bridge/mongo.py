import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()  # load from .env

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
MONGO_DB = os.getenv("MONGO_DB", "mydatabase")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]