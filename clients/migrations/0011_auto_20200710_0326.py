# Generated by Django 2.2 on 2020-07-10 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0010_client_clientinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='history',
            field=models.ManyToManyField(blank=True, related_name='appointments', related_query_name='appointment', to='appointments.Appointment'),
        ),
    ]
