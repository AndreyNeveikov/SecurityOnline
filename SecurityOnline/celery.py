import os
import time

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

from SecurityOnline.settings import CELERY_TASK_CALL_PERIOD_SECONDS

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'SecurityOnline.settings')

app = Celery('SecurityOnline')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'every': {
        'task': 'ServerActivityAnalyzer.tasks.repeat_order_make',
        'schedule': crontab(minute=f'*/{CELERY_TASK_CALL_PERIOD_SECONDS // 60}'),
    },

}


@app.task
def debug_task():
    time.sleep(15)
    print('adsdasd')
    return "заглушка"