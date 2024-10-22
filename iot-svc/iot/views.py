from flask import Blueprint, jsonify, request
from iot.tasks import process_data, hello_world, get_status
from iot.utils import get_farm_data

views = Blueprint("views", __name__)


@views.post("/")
def index():
    times = request.get_json()["times"]
    task = hello_world.apply_async(args=[times])
    return jsonify({"status": "success", "task_id": task.id}), 202


@views.post("/data")
def iot_data():
    data = request.get_json()
    farm_data = get_farm_data(data.get("farm_id"))
    if farm_data:
        task = process_data.apply_async(args=[data, farm_data])
        return jsonify({"status": "success", "task_id": task.id}), 202
    else:
        return jsonify({"status": "failed", "message": "farm not found"}), 404


@views.route("/task/<string:task_id>")
def check_task_status(task_id):
    """
    An endpoint to check the status of a task
    """
    response = get_status(task_id)
    return jsonify(response), 200
