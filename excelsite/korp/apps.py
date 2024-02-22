from django.apps import AppConfig


class KorpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'korp'
    verbose_name = 'Cайт по недвижимости'

    def ready(self):
        from  korp.models import Ofis
        from korp.models import Torg
        from korp.models import Tc
        from korp.models import Proizv
        from korp.models import Sklad
        from korp.models import Psn
        from korp.models import Land
        from korp.models import Flat

        from korp.signals import make_idl
