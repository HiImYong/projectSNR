from django.apps import AppConfig


class VisitorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'visitor'

    def ready(self):
        import racket.signals
