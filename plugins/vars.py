import os

API_ID    = os.environ.get("API_ID", "27192197")
API_HASH  = os.environ.get("API_HASH", "0019b60450debb66608795d488661cfc")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8113578720:AAGuDsG3Gqa6XkwurIFbQRX5y3LwrtbTeU8") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
