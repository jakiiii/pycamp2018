# Generated by Django 2.0.5 on 2018-05-18 08:44

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20180513_1759'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='eventparticipant',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='eventtrainer',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
