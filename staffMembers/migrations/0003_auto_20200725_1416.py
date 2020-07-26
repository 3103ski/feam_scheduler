# Generated by Django 2.2 on 2020-07-25 21:16

from django.conf import settings
from django.db import migrations, models
import staffMembers.models


class Migration(migrations.Migration):

    dependencies = [
        ('staffMembers', '0002_staffmember_supervisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffmember',
            name='createdBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(staffMembers.models.get_sentinel_user), related_name='staffMembers', to=settings.AUTH_USER_MODEL),
        ),
    ]