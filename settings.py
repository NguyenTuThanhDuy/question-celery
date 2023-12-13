CELERY_SETTINGS = {
    'broker_connection_retry_on_startup': True,
    'result_backend': 'redis://localhost:6379/0',
    'broker_url': 'pyamqp://guest@localhost//',
    'task_send_sent_event': True,
    'task_serializer': 'pickle',
    'result_serializer': 'pickle',
    'accept_content': ['pickle', 'json'],
}