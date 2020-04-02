web: gunicorn workinsights_v2.wsgi --chdir backend --limit-request-line 8188 --log-file -
worker: celery worker --workdir backend --app=workinsights_v2 --loglevel=info
