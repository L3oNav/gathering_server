from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RefiningConfig(AppConfig):
    name = "gathering_server.refining"
    verbose_name = _("Refining")

    def ready(self):
        try:
            import gathering_server.refining.signals # noqa F401
        except ImportError:
            pass
