# Generated by Django 4.0.3 on 2022-07-02 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='reminded',
            field=models.BooleanField(default=False),
        ),
    ]
