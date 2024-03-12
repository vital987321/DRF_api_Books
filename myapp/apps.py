#apps.py
from django.apps import AppConfig
from django.core.signals import request_started, request_finished
from myapp.api.signals import request_started_handler, request_finished_handler


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        request_started.connect(request_started_handler)
        request_finished.connect(request_finished_handler)
        import myapp.api.receivers
