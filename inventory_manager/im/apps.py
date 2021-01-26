from django.apps import AppConfig


class ImConfig(AppConfig):
    name = 'im'

    def ready(self):
        import im.signals
