class CeleryConfig:
    BROKER_URL = 'redis://127.0.0.1:6379/0'
    CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
    CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
    CELERYD_CONCURRENCY = 1
    CELERY_TIMEZONE = 'Asia/Shanghai'
