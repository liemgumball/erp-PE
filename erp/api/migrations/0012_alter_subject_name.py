# Generated by Django 5.0 on 2023-12-28 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_subject_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
