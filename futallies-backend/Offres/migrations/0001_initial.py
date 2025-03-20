# Generated by Django 5.1.5 on 2025-03-20 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('recruitment_email', models.EmailField(max_length=254)),
                ('size', models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], max_length=10)),
                ('website', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
                ('industry', models.CharField(blank=True, max_length=255, null=True)),
                ('founded_year', models.PositiveIntegerField(blank=True, null=True)),
                ('headquarters_location', models.CharField(blank=True, max_length=255, null=True)),
                ('number_of_employees', models.PositiveIntegerField(blank=True, null=True)),
                ('company_culture', models.TextField(blank=True, null=True)),
                ('social_media_links', models.JSONField(blank=True, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('awards_and_recognition', models.JSONField(blank=True, null=True)),
                ('benefits_overview', models.TextField(blank=True, null=True)),
                ('logo_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file_type', models.CharField(default='application/pdf', max_length=50)),
                ('file_content', models.BinaryField()),
                ('file_size', models.PositiveBigIntegerField()),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name="Titre de l'offre")),
                ('enterprise', models.CharField(max_length=255, verbose_name='Entreprise')),
                ('enterpriseLocation', models.CharField(max_length=255, null=True, verbose_name="Localisation de l'entreprise")),
                ('enterWebsite', models.URLField(blank=True, null=True, verbose_name="Site web de l'entreprise")),
                ('description', models.TextField(null=True, verbose_name="Description de l'offre")),
                ('domain', models.CharField(max_length=255, null=True, verbose_name="Domaine de l'offre")),
                ('location', models.CharField(max_length=255, null=True, verbose_name="Localisation de l'offre")),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Salaire')),
                ('duration', models.IntegerField(blank=True, null=True, verbose_name='Durée (en mois)')),
                ('type', models.CharField(choices=[('Job', 'Job'), ('Internship', 'Internship'), ('Other', 'Other')], max_length=20, verbose_name="Type d'offre")),
                ('requirements', models.TextField(blank=True, null=True, verbose_name='Exigences')),
                ('responsibilities', models.TextField(blank=True, null=True, verbose_name='Responsabilités')),
                ('educationLevel', models.CharField(blank=True, max_length=255, null=True, verbose_name="Niveau d'éducation requis")),
                ('experienceLevel', models.CharField(blank=True, max_length=255, null=True, verbose_name="Niveau d'expérience requis")),
                ('contractType', models.CharField(choices=[('CDI', 'CDI'), ('CDD', 'CDD')], default='CDD', max_length=3, verbose_name='Type de contrat')),
                ('benefits', models.TextField(blank=True, null=True, verbose_name='Avantages')),
                ('contactEmail', models.EmailField(max_length=254, null=True, verbose_name='Email de contact')),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed'), ('Pending', 'Pending')], default='Open', max_length=10, verbose_name="Statut de l'offre")),
                ('isRemote', models.BooleanField(default=False, verbose_name='Télétravail')),
                ('applicationMode', models.CharField(choices=[('Online', 'Online'), ('Physical', 'Physical'), ('Both', 'Both')], default='Online', max_length=10, verbose_name='Mode de candidature')),
                ('onlineSubmission', models.BooleanField(default=True, verbose_name='Soumission en ligne')),
                ('isRequiredCvDoc', models.BooleanField(default=True, verbose_name='CV requis')),
                ('isRequiredMlDoc', models.BooleanField(default=False, verbose_name='Lettre de motivation requise')),
                ('canAddOthersDoc', models.BooleanField(default=False, verbose_name='Autres documents autorisés')),
                ('applicationLink', models.URLField(blank=True, null=True, verbose_name='Lien de candidature')),
                ('additionalInfo', models.TextField(blank=True, null=True, verbose_name='Informations supplémentaires')),
                ('postedDate', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date de publication')),
                ('updatedAt', models.DateTimeField(auto_now=True, null=True, verbose_name='Dernière mise à jour')),
                ('expirationDate', models.DateTimeField(blank=True, null=True, verbose_name="Date d'expiration")),
            ],
            options={
                'verbose_name': 'Offre',
                'verbose_name_plural': 'Offres',
            },
        ),
        migrations.CreateModel(
            name='OfferApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Review', 'Review')], default='Accepted', max_length=20)),
                ('message', models.TextField(default="Je suis très intéressé(e) par cette offre et je suis convaincu(e) que mes compétences et mon expérience correspondent aux attentes de votre entreprise. J'aimerais avoir l'opportunité de discuter de cette offre plus en détail et de contribuer au succès de votre équipe.")),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('submitted_documents_ids', models.JSONField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
