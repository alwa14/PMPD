# Generated by Django 4.2.3 on 2023-09-29 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mqttdata',
            name='current',
            field=models.FloatField(default=0.0),
        ),
    ]
