# Generated by Django 2.2 on 2020-07-09 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_client_history'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='clientCreatedOn',
            new_name='createdOn',
        ),
    ]
