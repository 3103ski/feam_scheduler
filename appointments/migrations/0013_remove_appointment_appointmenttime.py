# Generated by Django 2.2 on 2020-07-13 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0012_appointment_appointmenttime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appointmentTime',
        ),
    ]
