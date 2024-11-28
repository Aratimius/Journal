from time import sleep

from django.apps import AppConfig


class RecordsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "records"

#  РАСКОММЕНТИРОВАТЬ КОД ДЛЯ АВТОМАТИЗАЦИИ ОТПРАВКИ РАССЫЛОК -> ЗАПУСТИТЬ СЕРВЕР
    def ready(self):
        from records.services import start_sheduler
        sleep(2)
        start_sheduler()
