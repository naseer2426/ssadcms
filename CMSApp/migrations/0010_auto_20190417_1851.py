# Generated by Django 2.2 on 2019-04-17 10:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CMSApp', '0009_auto_20190407_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 17, 10, 51, 13, 477563, tzinfo=utc)),
        ),
    ]
