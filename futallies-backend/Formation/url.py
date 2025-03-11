from django.urls import path
from . import views
from .views import ContentView, ChapitreView

urlpatterns = [
    path('modules/create/', views.create_module, name='create_module'),
    path('domaines/list_domaines', views.list_domaines, name='list_domaines'), 
##########################################################################################
    path('domaines/create/', views.create_domaine, name='create_domaine'),
    path('modules/list_modules', views.list_modules, name='list_modules'), 
##########################################################################################
    path('cours/create/', views.create_cours, name='create_cours'),
    path('cours/list_cours', views.list_cours, name='list_cours'), 
##########################################################################################
    path('chapitre/create/', views.create_chapitre, name='create_chapitre'),
    path('chapitre/list_chapitres', views.list_chapitres, name='list_chapitres'), 

##########################################################################################
    path('section/create/', views.create_section, name='create_sectioon'),
    path('section/list_sections', views.list_section, name='list_sectioon'),
##########################################################################################
    path('contenu/create/', views.create_contenu, name='create_contenu'),
    path('contenus/list_contenus', views.list_contenus, name='list_contenus'),
    path('contenu/update-contenu/', views.update_contenu, name='create_contenu'),
    #########################################################################################
    path('contenu/<int:contenu_id>/', ContentView.as_view(), name='detail_contenu'), 
    #########################################################################################
    path('chapitre/<int:chapitre_id>/', ChapitreView.as_view(), name='detail_chapitre'), 

#########################################################################################

    # Liste des webinaires
    path('webinars/', views.list_webinars, name='list_webinars'),

    # Détails d'un webinaire
    path('webinars/<int:webinar_id>/', views.get_webinar_detail, name='get_webinar_detail'),

    # Création d'un webinaire
    path('webinars/create/', views.create_or_update_webinar, name='create_webinar'),

    # Mise à jour d'un webinaire
    path('webinars/<int:webinar_id>/update/', views.update_webinar, name='update_webinar'),

    # Suppression d'un webinaire
    path('webinars/<int:webinar_id>/delete/', views.delete_webinar, name='delete_webinar'),
    path('webinarEnrollments/enroll', views.enroll_to_webinar, name='inscrit'),
        # Liste des webinaires
    path('webinars-inscrit/', views.list_webinars_inscrit, name='list_webinars'),

]





