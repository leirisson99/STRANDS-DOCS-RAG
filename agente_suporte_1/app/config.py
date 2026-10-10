import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
MODEL_ID = os.getenv("MODEL_ID", "gpt-6-luna")
SESSIONS_DIR = os.get("SESSIONS_DIR", "./sessions")


