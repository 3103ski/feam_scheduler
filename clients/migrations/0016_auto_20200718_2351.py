# Generated by Django 2.2 on 2020-07-19 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0015_auto_20200711_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='clientDescription',
            new_name='clientNotes',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='phoneNumber',
            new_name='contactNumber',
        ),
    ]
