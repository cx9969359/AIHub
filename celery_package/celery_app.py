from celery import Celery

from celery_package.celery_config import CeleryConfig

app = Celery('celery_package', include=['celery_package.tasks'])
app.config_from_object(CeleryConfig)

if __name__ == '__main__':
    app.start()
