from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from piccolo.engine import engine_finder
from piccolo_admin.endpoints import create_admin
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

from accounts.endpoints import accounts_router
from home.endpoints import HomeEndpoint
from home.piccolo_app import APP_CONFIG
from settings import ORIGINS

app = FastAPI(
    routes=[
        Route("/", HomeEndpoint),
        Mount(
            "/admin/",
            create_admin(
                tables=APP_CONFIG.table_classes,
                # Required when running under HTTPS:
                # allowed_hosts=['my_site.com']
            ),
        ),
        Mount("/static/", StaticFiles(directory="static")),
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(accounts_router)


@app.on_event("startup")
async def open_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.start_connection_pool()
    except Exception as e:
        print(f"Unable to connect to the database: {e}")


@app.on_event("shutdown")
async def close_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.close_connection_pool()
    except Exception as e:
        print(f"Unable to connect to the database: {e}")
