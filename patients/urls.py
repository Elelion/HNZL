from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from patients import views
from patients.views import *


app_name = 'patients'

urlpatterns = [
    path('all/', login_required(BrowseListView.as_view()), {'page': 1}, name='browse'),
    path('all/<int:page>/', login_required(BrowseListView.as_view()), name='browse'),


    path('dispensary/', login_required(DispensaryListView.as_view()), {'page': 1}, name='dispensary'),
    path('dispensary/<int:page>/', login_required(DispensaryListView.as_view()), name='dispensary'),

    path('search/', search, name='search'),
    path('add/', add, name='add'),

    path('patients/edit/<int:patient_id>/', views.edit, name='edit'),
    path('patients/delete/<int:patient_id>/', views.delete, name='delete'),
]
