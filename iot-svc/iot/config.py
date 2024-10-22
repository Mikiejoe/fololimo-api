import os
from dataclasses import dataclass
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

@dataclass
class BaseConfig(object):
    SECRET_KEY: str = os.urandom(20)
    DEBUG: bool = False
    TESTING: bool = False

    # celery configurations
    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND: str = os.getenv("CELERY_RESULT_BACKEND")
    TASK_IGNORE_RESULT:bool = True # basically, we tell celery to igore results of the workers unless we

    @staticmethod
    def init_app(app):
       pass


@dataclass
class DevelopmentConfig(BaseConfig):
    DEBUG: bool = True
    SQLALCHEMY_DATABASE_URI: str = os.environ.get(
        "DATABASE_URL", os.path.join("sqlite:////" + BASE_DIR, "tiller.sqlite")
    )
    SQLALCHEMY_TRACK_MODIFICATION: bool = False
    SQLALCHEMY_ECHO: bool = False

@dataclass
class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI: str = "sqlite://"
    TESTING: bool = True


@dataclass
class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI: str = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATION: bool = False
    SQLALCHEMY_ECHO: bool = False


config_dict = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}