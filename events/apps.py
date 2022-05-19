from django.apps import AppConfig


# the app class to installed to the project in todolist/settings.py
class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events'
