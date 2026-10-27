import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CAT_API_KEY = os.getenv("THE_CAT_API_KEY")
PROXY_URL = os.getenv("PROXY_URL") or None

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found in .env")
