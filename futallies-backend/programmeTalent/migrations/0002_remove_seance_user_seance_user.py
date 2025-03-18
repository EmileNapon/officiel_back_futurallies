# Generated by Django 4.2.19 on 2025-03-18 13:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('programmeTalent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seance',
            name='user',
        ),
        migrations.AddField(
            model_name='seance',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
