# Generated by Django 2.2.1 on 2019-09-18 20:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 9, 18, 20, 6, 42, 519770, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 18, 20, 6, 42, 515770, tzinfo=utc)),
        ),
    ]