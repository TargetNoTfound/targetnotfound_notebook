# Generated by Django 2.0.2 on 2018-04-24 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoiveRe', '0003_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
