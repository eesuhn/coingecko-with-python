import os

from dotenv import load_dotenv


load_dotenv()

CG_API_KEY = os.getenv("CG_API_KEY")
if not CG_API_KEY:
    print("No API key found. Please provide one in .env")
