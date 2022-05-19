from django.contrib import admin

# added
from .models import Event

# Register your models here.
# added: register the models of apps to the admin app for the administrator to
# maintain their data
admin.site.register(Event)
