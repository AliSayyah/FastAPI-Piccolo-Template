from starlette.config import Config


def generate_secret_key():
    import secrets

    return secrets.token_urlsafe(32)


# Configuration from environment variables or '.env' file.
config = Config(".env")

# main database
DB_NAME = config("DB_NAME", default="postgres")
DB_USER = config("DB_USER", default="postgres")
DB_PASSWORD = config("DB_PASSWORD", default="postgres")
DB_HOST = config("DB_HOST", default="db")
DB_PORT = config("DB_PORT", default=5432)

# test database
DB_TEST_USER = config("DB_TEST_USER", default="postgres")
DB_TEST_PASSWORD = config("DB_TEST_PASSWORD", default="postgres")
DB_TEST_NAME = config("DB_TEST_NAME", default="test")
DB_TEST_HOST = config("DB_TEST_HOST", default=DB_HOST)
DB_TEST_PORT = config("DB_TEST_PORT", default=DB_PORT)

SECRET_KEY = config("SECRET_KEY", default=generate_secret_key())
RELOAD = config("RELOAD", default=True)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ORIGINS = [
    "http://localhost:8000",
]
