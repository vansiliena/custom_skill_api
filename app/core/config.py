import os
from dotenv import load_dotenv

load_dotenv()

class Setting:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME")



settings = Setting()