from dotenv import load_dotenv
import os

load_dotenv()

INSTANCE = os.getenv("INSTANCE")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")