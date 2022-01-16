from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine

from settings import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER

DB = PostgresEngine(
    config={
        "database": DB_NAME,
        "user": DB_USER,
        "password": DB_PASSWORD,
        "host": DB_HOST,
        "port": DB_PORT,
    }
)

APP_REGISTRY = AppRegistry(
    apps=[
        "home.piccolo_app",
        "piccolo_admin.piccolo_app",
        "augmented_reality.piccolo_app",
        "accounts.piccolo_app",
    ]
)
