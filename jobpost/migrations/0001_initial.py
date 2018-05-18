# Generated by Django 2.0.5 on 2018-05-18 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selection_confirmation', models.BooleanField(default=False)),
                ('call_for_interview', models.BooleanField(default=False)),
                ('applicant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.PersonalProfile')),
            ],
        ),
        migrations.CreateModel(
            name='JobApplicantManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='JobPostBasic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=256)),
                ('salary_range', models.CharField(max_length=256)),
                ('is_part_time', models.BooleanField(default=False)),
                ('position', models.CharField(max_length=256)),
                ('stack', models.TextField()),
                ('vacancy', models.PositiveIntegerField()),
                ('deadline', models.DateField()),
                ('organization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.OrganizationProfile')),
            ],
            options={
                'permissions': (('view_post', 'Can see job post'),),
            },
        ),
        migrations.CreateModel(
            name='JobPostDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('application_process', models.TextField()),
                ('screening_details', models.TextField()),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobpost.JobPostBasic')),
            ],
        ),
        migrations.AddField(
            model_name='jobapplicant',
            name='job_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobpost.JobPostBasic'),
        ),
    ]
