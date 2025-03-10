# Generated by Django 4.2.19 on 2025-03-06 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Offres', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='offerapplication',
            name='candidat',
            field=models.ForeignKey(default=16, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='offerapplication',
            name='offer',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Offres.offer'),
        ),
        migrations.AddField(
            model_name='offer',
            name='createdBy',
            field=models.ForeignKey(default='16', on_delete=django.db.models.deletion.CASCADE, related_name='offers', to=settings.AUTH_USER_MODEL, verbose_name='Créé par'),
        ),
        migrations.AlterUniqueTogether(
            name='offerapplication',
            unique_together={('offer', 'candidat')},
        ),
    ]
