# from __future__ import absolute_import, unicode_literals
# import os

# from celery import Celery
# from django.conf import settings

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'texttoimage.settings')

# app = Celery('texttoimage', broker='redis://localhost:6379/0')
# app.conf.enable_utc = False
# app.conf.update(timezone = 'Asia/Kolkata')
# app.config_from_object(settings, namespace='CELERY')
# app.autodiscover_tasks()

# @app.task(bind = True)
# def debug_task(self):
#     print(f'Request : {self.reuqest!r}')


from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'texttoimage.settings')
# os.environ.setdefault("FORKED_BY_MULTIPROCESSING", "1")

app = Celery('texttoimage')

# Load task modules from all registered Django app configs.
app.config_from_object("django.conf:settings", namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
