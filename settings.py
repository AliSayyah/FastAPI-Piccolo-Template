from starlette.config import Config

# Configuration from environment variables or '.env' file.
config = Config(".env")

# main database
DB_NAME = config("DB_NAME")
DB_USER = config("DB_USER")
DB_PASSWORD = config("DB_PASSWORD")
DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT")

# test database
DB_TEST_USER = config("DB_TEST_USER")
DB_TEST_PASSWORD = config("DB_TEST_PASSWORD")
DB_TEST_NAME = config("DB_TEST_NAME")
DB_TEST_HOST = DB_HOST
DB_TEST_PORT = DB_PORT


SECRET_KEY = config("SECRET_KEY")
RELOAD = config("RELOAD")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ORIGINS = [
    "http://localhost:8000",
]
