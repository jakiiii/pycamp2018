# Generated by Django 2.0.5 on 2018-05-19 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20180519_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventparticipant',
            name='participant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_participant', related_query_name='participant', to=settings.AUTH_USER_MODEL),
        ),
    ]