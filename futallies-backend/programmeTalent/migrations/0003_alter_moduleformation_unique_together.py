# Generated by Django 5.1.5 on 2025-03-20 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Formation', '0002_initial'),
        ('programmeTalent', '0002_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='moduleformation',
            unique_together={('module', 'formation')},
        ),
    ]
