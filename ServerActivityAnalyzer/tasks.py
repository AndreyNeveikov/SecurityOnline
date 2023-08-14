from SecurityOnline.celery import app
from ServerActivityAnalyzer.controllers import ping_servers_list


@app.task
def ping_servers_list_task():
    ping_servers_list()
    return None
