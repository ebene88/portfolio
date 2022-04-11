from django.apps import AppConfig

import sys
sys.setrecursionlimit(1500)
class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
