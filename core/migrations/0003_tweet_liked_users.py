# Generated by Django 3.1.7 on 2021-04-10 18:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_remove_tweet_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='liked_users',
            field=models.ManyToManyField(related_name='liked_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
