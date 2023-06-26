import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "watarget.settings")
app = Celery("watarget")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()