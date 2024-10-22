import time
from celery.result import AsyncResult
from celery import shared_task
from iot.utils import aggregate_the_data, chat_model, get_weather_data
from iot.database import upload_to_firebase


@shared_task(name="process_data", bind=True, ignore_result=False, autoretry_for=(Exception,), retry_kwargs={'max_retries': 3, 'countdown': 5})
def process_data(self, iot_data, farm_data):
    self.update_state(state="PROGRESS", meta={"remaining": 1, "completed": 0, "message": "task started successfully"})
    weather_data = get_weather_data(farm_data.get("location"))
    model_data = aggregate_the_data(iot_data, farm_data, weather_data)
    model_output = chat_model(model_data, farm_data.get("user"), farm_data.get("id"))
    upload_to_firebase(model_output)
    print("The data was successfully uploaded to firebase ..")
    return {"remaining": 0,"completed": 1, "result": "All tasks completed"}

@shared_task(name="hello_world", bind=True, ignore_result=False, autoretry_for=(Exception,), retry_kwargs={'max_retries': 3, 'countdown': 5})
def hello_world(self, times):
    for i in range(times):
        time.sleep(2)
        self.update_state(state="PROGRESS", meta={"remaining": times - i, "completed": i, "message": "task in progress ..."})
    return {"remaining": 0,"completed": 1, "result": "All tasks completed",}


# check the status of a task (reusable view function)
def get_status(task_id):
    task = AsyncResult(task_id)
    if task.state == "PENDING":
        # The task is not started yet
        response = {
            "state": task.state,
            "remaining": 1,
            "completed": 0,
            "status": "Pending ...."
        }

    elif task.state != "FAILURE":
        response = {
            "state": task.state,
            "remaining": task.info.get("remaining"),
            "completed": task.info.get("completed"),
            "message": task.info.get("message", "")
        }
        if "result" in task.info:
            response["result"] = task.info["result"]

    else:
        response = {
            "state": task.state,
            "remaining": 1,
            "completed": 0,
            "status": str(task.info)
        }
    return response