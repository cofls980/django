# Generated by Django 3.0.3 on 2020-02-29 19:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Prac1', '0002_auto_20200301_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 29, 19, 44, 26, 323604, tzinfo=utc), verbose_name='date published'),
        ),
    ]