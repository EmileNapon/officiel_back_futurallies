# Generated by Django 4.2.19 on 2025-03-10 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='fonction',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('apprenant', 'Apprenant'), ('employeur', 'Employeur'), ('formateur', 'Formateur')], default='apprenant', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='specialite',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
