from django.apps import AppConfig


class MentcareApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mentcare_api'
    def ready(self):
        from scheduler import scheduler
        scheduler.start()
