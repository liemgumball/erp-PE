# Generated by Django 5.0 on 2023-12-25 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_payment_paidamount_alter_payment_paid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='paidAmount',
            new_name='paid_amount',
        ),
    ]