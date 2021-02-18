from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GatheringConfig(AppConfig):
    name = "gathering_server.gathering"
    verbose_name = _("Gathering")

    def ready(self):
        try:
            import gathering_server.gathering.signals # noqa F401
        except ImportError:
            pass
