# from __future__ import absolute_import
# import os
# from celery import Celery
# from django.conf import settings
#
# #from app.tasks import test_celery
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
#
# app = Celery('app')
#
# CELERY_TIMEZONE = 'UTC'
#
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
#
#
# print('-------- TEST CELERY -----------------')
# # test_celery()


from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from app import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('useid')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
