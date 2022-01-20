from starlette.config import Config

# Configuration from environment variables or '.env' file.
config = Config(".env")
DB_NAME = config("DB_NAME")
DB_USER = config("DB_USER")
DB_PASSWORD = config("DB_PASSWORD")
DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT")
SECRET_KEY = config("SECRET_KEY")
RELOAD = config("RELOAD")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ORIGINS = [
    "http://localhost:8000",
]
