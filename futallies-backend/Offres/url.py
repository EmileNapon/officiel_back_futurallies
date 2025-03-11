from django.urls import path
from . import views
from .views import (
    EnterpriseView, EnterpriseDetailView,
    OfferView, OfferDetailView, FileDetailView,
    OfferApplicationView, OfferApplicationDetailView, FileView, OfferApplicationView1
)

urlpatterns = [
    # Routes for Enterprise
    path('enterprises/', EnterpriseView.as_view(), name='enterprise-list-create'),
    path('enterprises/<int:pk>/', EnterpriseDetailView.as_view(), name='enterprise-detail'),



    # Routes for Offer
    path('offers/', OfferView.as_view(), name='offer-list-create'),
    path('offers/<int:pk>/', OfferDetailView.as_view(), name='offer-detail'),

#    path('offer-applications/create', OfferApplicationView.as_view(), name='offer-create'),



    path('files/create', FileView.as_view(), name='file-list-create'),
    path('files/<int:pk>/', FileDetailView.as_view(), name='file-detail'),

    # Routes for OfferApplication
    path('offer-applications', OfferApplicationView.as_view(), name='application-list-create'),
    path('applications/<int:pk>/', OfferApplicationDetailView.as_view(), name='application-detail'),
    path('offer-applications/<int:pk>/', OfferApplicationView1.as_view(), name='offer-application-list'),

]
