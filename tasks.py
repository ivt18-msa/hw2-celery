import os
from time import sleep
from celery import Celery

celery_app = Celery(__name__, backend='redis://localhost', broker='redis://localhost')


@celery_app.task
def arhive_file(filename):
    sleep(15)
    os.system(f'echo {filename}')  # TODO: архивация
    sleep(15)
    return filename
