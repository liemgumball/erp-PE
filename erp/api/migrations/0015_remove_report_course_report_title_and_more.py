# Generated by Django 5.0 on 2023-12-29 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_course_end_date_alter_course_start_date_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='course',
        ),
        migrations.AddField(
            model_name='report',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='report',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
