# Generated by Django 3.0.3 on 2020-02-29 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('pid', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('Color', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('pid', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('ptext', models.CharField(max_length=20)),
            ],
        ),
    ]
