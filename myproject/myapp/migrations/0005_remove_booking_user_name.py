# Generated by Django 5.1.7 on 2025-03-09 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_booking_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user_name',
        ),
    ]
