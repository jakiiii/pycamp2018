# Generated by Django 2.0.5 on 2018-05-13 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('jobpost', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='jobapplicant',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='jobpostbasic',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='jobpostbasic',
            name='organization_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jobpostdetails',
            name='job_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jobpost.JobPostBasic'),
        ),
    ]
