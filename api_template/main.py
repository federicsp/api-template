from fastapi import FastAPI
from app.routes.users import router as users_router
from fastapi.openapi.utils import get_openapi

app = FastAPI()

app.include_router(users_router)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="API-template",
        version="0.1.0",
        description="The project is a simple API for managing user information.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
