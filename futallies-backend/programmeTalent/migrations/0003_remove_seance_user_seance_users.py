# Generated by Django 4.2.19 on 2025-03-18 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('programmeTalent', '0002_remove_seance_user_seance_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seance',
            name='user',
        ),
        migrations.CreateModel(
            name='Seance_users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seance', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='programmeTalent.seance')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
