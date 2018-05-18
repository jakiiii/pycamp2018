# Generated by Django 2.0.5 on 2018-05-18 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalRecommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rec_event', to='events.EventDetail')),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='userprofile.PersonalProfile')),
                ('trainer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rec_trainer', to='userprofile.PersonalProfile')),
            ],
        ),
    ]
