from piccolo_conf import *  # noqa

from settings import DB_TEST_NAME, DB_TEST_USER, DB_TEST_PASSWORD, DB_TEST_HOST, DB_TEST_PORT

DB = PostgresEngine(
    config={
        "database": DB_TEST_NAME,
        "user": DB_TEST_USER,
        "password": DB_TEST_PASSWORD,
        "host": DB_TEST_HOST,
        "port": DB_TEST_PORT,
    }
)
