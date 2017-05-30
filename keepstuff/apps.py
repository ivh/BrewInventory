from django.apps import AppConfig


class KeepstuffConfig(AppConfig):
    name = 'keepstuff'
    def ready(self):
        import keepstuff.signals
