# Generated by Django 2.2 on 2020-07-13 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0015_auto_20200711_1730'),
        ('appointments', '0015_appointment_appointmentnotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointment', to='clients.Client'),
        ),
    ]
