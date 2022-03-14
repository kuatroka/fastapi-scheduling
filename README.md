# Launch Redis through docker to be used for celery

'''
docker run -it --rm -p 6380:6380 redis --port 6380
'''

# Launch Celery worker

'''
celery --app app.worker.celery_app worker --loglevel INFO
'''

# Celery with beat for periodic tasks

'''
celery --app app.worker.celery_app beat --loglevel INFO
'''

# Celery worker with beat (it seems like it is not working on Windows)

'''
celery --app app.worker.celery_app worker --beat -s celerybeat-schedule --loglevel INFO
'''
