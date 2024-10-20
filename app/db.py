from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
def getDb():
    mongo_uri= os.getenv("MONGO_URI")
    client  = MongoClient(mongo_uri)
    return client
