# Generated by Django 2.0.5 on 2018-05-17 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20180512_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalprofile',
            name='is_student',
            field=models.BooleanField(default=True),
        ),
    ]