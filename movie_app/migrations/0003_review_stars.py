# Generated by Django 4.1.4 on 2022-12-24 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_movie_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
