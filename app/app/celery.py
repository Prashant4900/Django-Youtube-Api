from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

# from . import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')


app = Celery('app')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))


app.conf.beat_schedule = {
    # Fetching the youtube videos every 5 mins
    "add_videos_in_database_task": {
        "task": 'add_videos_in_database',
        "schedule": crontab(minute="*/5"),
    },
}
