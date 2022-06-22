# added
import datetime
from django.utils import timezone

from django.db import models

# added
from django.contrib.auth.models import User

# Create your models here.
# added: model class
#-
class Event(models.Model):
    # member variables names are also fields names
    # no need to assign primary key since django automatically generates a
    # primary key (id)
    # - foreign key (object, the corresponding field name is the object name
    # - plus "_id" suffix, here is "user_id"): the corresponding field is the
    # - primary key in another table (here is User)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
