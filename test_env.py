from dotenv import load_dotenv
import os

load_dotenv()

print("TOKEN:", os.getenv("GITHUB_TOKEN"))
print("OWNER:", os.getenv("GITHUB_OWNER"))
print("REPO:", os.getenv("GITHUB_REPO"))
print("DB:", os.getenv("DATABASE_URL"))
