from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # This function is used to import the signals when the app is ready.
    def ready(self):
        import users.signals