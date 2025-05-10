from celery import Celery
from config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

celery_app = Celery('tasks',
                    broker=CELERY_BROKER_URL,
                    backend=CELERY_RESULT_BACKEND)

@celery_app.task
def heavy_computation(n):
    """Функция, имитирующая тяжёлые вычисления"""
    result = sum(i * i for i in range(n))
    return result