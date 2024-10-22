from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
import json

from iot.config import config_dict
from iot.views import views
from iot.celery import celery_init_app

def create_app(config: str = "default") -> Flask:

    app = Flask(__name__)
    app.config.from_object(config_dict[config])
    celery_init_app(app=app)

    @app.route("/api/healthcheck")
    def index():
        return jsonify({"message": "Hello world"}), 200
    app.register_blueprint(views, url_prefix="/v1")

    """ handle any other exception """
    @app.errorhandler(HTTPException)
    def handle_exceptions(error):
        response = error.get_response()
        response.data = json.dumps({
            "status code": error.code,
            "name": error.name,
            "description": error.description,
        })
        response.content_type = "application/json"
        return response

    return app