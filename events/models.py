# added
import datetime
from django.utils import timezone

from django.db import models

# Create your models here.
# added: model class
#-
class Event(models.Model):
    # member variables names are also fields names
    # no need to assign primary key since django automatically generates a
    # primary key (id)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    # specifying a verbose_name ("time to remind") to show in admin app (instead
    # of "time") (optionally)
    time = models.DateTimeField('time to remind')
    # the string representation of the object.
    def __str__(self):
        return self.title
    def unexpired(self):
        # using timezone.now() since USE_TZ set in todolist/settings.py
        return self.time >= timezone.now()
