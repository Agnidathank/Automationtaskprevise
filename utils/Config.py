import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://defaulturl.com/")
