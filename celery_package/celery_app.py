from __future__ import absolute_import, unicode_literals

from celery import Celery

from celery_package.celery_config import CeleryConfig

app = Celery('celery_package', include=['celery_package.tasks'])
app.config_from_object(CeleryConfig)


@app.task
def add(x, y):
    return x + y
