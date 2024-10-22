from django.apps import AppConfig


class FololimoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fololimo'

    def ready(self):
        import fololimo.signals
