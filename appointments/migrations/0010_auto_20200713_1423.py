# Generated by Django 2.2 on 2020-07-13 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0009_remove_appointment_appointmenttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointmentDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
