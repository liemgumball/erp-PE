# Generated by Django 5.0 on 2023-12-28 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_subject_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='video',
            field=models.CharField(default='kAM1PulT0Ns', max_length=255),
        ),
    ]
