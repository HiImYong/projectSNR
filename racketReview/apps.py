from django.apps import AppConfig


class racketReviewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'racketReview'

    def ready(self):
        import racket.signals
