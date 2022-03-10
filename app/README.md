# Launche Redis through docker to be used for celery

'''
docker run -it --rm -p 6300:6300 redis --port 6300
'''

# Launch Celery

'''
celery --app app.worker.celery_app worker --loglevel INFO
'''
