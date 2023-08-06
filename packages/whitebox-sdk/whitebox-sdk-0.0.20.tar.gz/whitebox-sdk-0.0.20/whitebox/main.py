from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from whitebox.api.v1 import v1_router
from fastapi.openapi.utils import get_openapi
from whitebox.api.v1.docs import (
    tags_metadata,
    validation_error,
    authorization_error,
    not_found_error,
    conflict_error,
    content_gone,
    bad_request,
)
from whitebox.core.settings import get_settings
from whitebox.core.db import connect, close
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError

from whitebox.utils.errors import errors

settings = get_settings()

app = FastAPI(title=settings.APP_NAME, redoc_url="/")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router)


app.add_exception_handler(StarletteHTTPException, errors.http_exception_handler)
app.add_exception_handler(RequestValidationError, errors.validation_exception_handler)


@app.on_event("startup")
async def on_app_start():
    """Anything that needs to be done while app starts"""
    await connect()


@app.on_event("shutdown")
async def on_app_shutdown():
    """Anything that needs to be done while app shutdown"""
    await close()


def app_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Whitebox",
        version=settings.VERSION,
        routes=app.routes,
        tags=tags_metadata,
    )

    openapi_schema["components"]["schemas"]["HTTPValidationError"] = validation_error
    openapi_schema["components"]["schemas"]["AuthorizationError"] = authorization_error
    openapi_schema["components"]["schemas"]["NotFoundError"] = not_found_error
    openapi_schema["components"]["schemas"]["ConflictError"] = conflict_error
    openapi_schema["components"]["schemas"]["BadRequest"] = bad_request
    openapi_schema["components"]["schemas"]["ContentGone"] = content_gone

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = app_openapi
