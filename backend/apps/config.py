import os


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./paygyaan.db")
OPENAI_KEY = os.getenv("OPENAI_KEY")