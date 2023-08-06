from backend.config import settings
from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise


def init_db(app: FastAPI):
    register_tortoise(
        app,
        db_url=settings.DATABASE_URL,
        modules={"models": settings.APP_MODELS},
        generate_schemas=True,
        add_exception_handlers=True,
    )


Tortoise.init_models(settings.APP_MODELS, "models")
