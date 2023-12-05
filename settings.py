CELERY_SETTINGS = {
    'CELERY_ENABLE_UTC': True,
    'CELERY_RESULT_BACKEND': 'redis://localhost:6379/0',
    'BROKER_URL': 'redis://localhost:6379/0',
    'CELERY_SEND_TASK_SENT_EVENT': True,
    'CELERY_TASK_SERIALIZER': 'pickle',
    'CELERY_RESULT_SERIALIZER': 'pickle',
    'CELERY_ACCEPT_CONTENT': ['pickle', 'json'],
}