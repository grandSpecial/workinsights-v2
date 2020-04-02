from django.core import management

from workinsights_v2.celery import app as celery_app


@celery_app.task
def clearsessions():
    management.call_command('clearsessions')
