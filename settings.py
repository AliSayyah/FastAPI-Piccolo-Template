from starlette.config import Config


def generate_secret_key():
    import secrets

    return secrets.token_urlsafe(32)


# Configuration from environment variables or '.env' file.
config = Config(".env")

# main database
DB_NAME = config("DB_NAME", cast=str, default="postgres")
DB_USER = config("DB_USER", cast=str, default="postgres")
DB_PASSWORD = config("DB_PASSWORD", cast=str, default="postgres")
DB_HOST = config("DB_HOST", cast=str, default="db")
DB_PORT = config("DB_PORT", cast=int, default=5432)

# test database
DB_TEST_USER = config("DB_TEST_USER", cast=str, default="postgres")
DB_TEST_PASSWORD = config("DB_TEST_PASSWORD", cast=str, default="postgres")
DB_TEST_NAME = config("DB_TEST_NAME", cast=str, default="test")
DB_TEST_HOST = config("DB_TEST_HOST", cast=str, default=DB_HOST)
DB_TEST_PORT = config("DB_TEST_PORT", cast=int, default=DB_PORT)


SECRET_KEY = config("SECRET_KEY", default=generate_secret_key())
RELOAD = config("RELOAD", cast=bool, default=True)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ORIGINS = [
    "http://localhost:8000",
]
