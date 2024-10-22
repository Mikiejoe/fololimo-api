import os
from dotenv import load_dotenv
from iot import create_app

load_dotenv()
config = os.getenv("APP_ENV") or "default"
app = create_app(config)