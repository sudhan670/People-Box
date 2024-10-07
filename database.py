from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# MongoDB connection details
MONGO_DETAILS = os.getenv("MONGO_DETAILS")
print(MONGO_DETAILS)
# Connect to MongoDB
client = AsyncIOMotorClient(MONGO_DETAILS)

# Specify database and collections
database = client.job_recommendation_db
user_profiles_collection = database.get_collection("user_profiles")
job_postings_collection = database.get_collection("job_postings")
