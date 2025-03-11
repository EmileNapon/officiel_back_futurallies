from django.urls import path
from . import views
# from .views import(EncadrantAPIView)

urlpatterns = [

    path('fidalli/formation/create', views.create_Formation, name='create_formation'),
    path('fidalli/formation/<int:pk>/update/', views.update_formation, name='update_formation'),
    path('fidalli/formation/list-formations/<int:formation_id>/', views.detail_formation, name='detail_formation'),
    path('fidalli/formation/list-formations/', views.list_formations, name='list_formation'), 
    path('fidalli/formations/<int:formation_id>/remove/', views.remove_formation, name='remove_formation'),
    ################################################################################
    path('fidalli/inscrit/create/', views.create_Inscrit, name='create_inscrit'),
    path('fidalli/inscrit/listes_inscrits/', views.liste_Inscrits, name='liste_Inscrits'),
    ################################################################################
    path('fidalli/ModuleFormation/create/', views.create_module_formation, name='ModuleFormation'),
    path('fidalli/ModuleFormation/list_moduleFormation/', views.list_ModuleFormation, name='ModuleFormation'),
    path('fidalli/formations/<int:formation_id>/modules/<int:module_id>/remove/', views.remove_module_from_formation, name='remove_module_from_formation'),
    ################################################################################
    path('fidalli/seance/create/', views.create_Seance, name='create_seance'),
    path('fidalli/seance/list_seances/', views.list_Seance, name='list_seances'),
    path('fidalli/seances/<int:pk>/delete/', views.delete_seance, name='delete_seance'),
    path('fidalli/seance/<int:pk>/update/', views.update_Seance, name='update_seances'),
    path('fidalli/seances/liste-seance/<int:seance_id>/', views.detail_Seance, name='detail_Seance'),

    ################################################################################
    path('fidalli/group/create/', views.create_Group, name='create_group'),
    path('fidalli/affectationStage/create/', views.create_AffectationStage, name='AffectationStage'),
    ######################################################################################

    path('fidalli/annonces', views.annonce, name='annonce'),
    path('fidalli/annonces/<int:annonce_id>/', views.annonce_detail, name='annonce_detail'),
    
    # path('encadrant/', EncadrantAPIView.as_view(), name='encadrant'),
    
]




