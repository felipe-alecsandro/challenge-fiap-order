from django.apps import AppConfig

class BurgerstoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'burgerstore'

    def ready(self):
        # Your initialization code here
        pass
