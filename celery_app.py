from celery import Celery
import os
import sys

# Ensure the src directory is in the sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils.config_manager import get_config_manager_singleton
configManager = get_config_manager_singleton()

app = Celery('tasks', broker=configManager.celery.broker_url, backend=configManager.celery.result_backend)
app.conf.update(result_expires=3600, task_serializer='json', accept_content=['json'], result_serializer='json')

if __name__ == '__main__':
    app.start()
