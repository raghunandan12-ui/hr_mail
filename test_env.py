import os
from dotenv import load_dotenv

load_dotenv()

print("EMAIL:", os.getenv("EMAIL"))
print("PASSWORD:", os.getenv("PASSWORD"))
