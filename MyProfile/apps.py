from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class MyprofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MyProfile'
    verbose_name = 'CEDROUSEROLL OMONDI'


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
