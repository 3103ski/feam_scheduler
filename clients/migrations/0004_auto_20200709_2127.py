# Generated by Django 2.2 on 2020-07-09 21:27

import clients.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20200709_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='createdBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(clients.models.get_sentinel_user), to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='client',
            name='lastModified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
