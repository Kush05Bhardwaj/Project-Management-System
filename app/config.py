import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file if present

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret-key')
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/mini_pms')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-secret-key')