# Generated by Django 3.0.3 on 2020-02-07 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0002_auto_20200206_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_id',
            field=models.IntegerField(default=0),
        ),
    ]
