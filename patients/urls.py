from django.urls import path

from patients import views
from patients.views import *


app_name = 'patients'

urlpatterns = [
    path('browse/', browse, name='browse'),
    path('page/<int:page_number>', browse, name='paginator'),

    path('search/', search, name='search'),
    path('add/', add, name='add'),

    path('patients/edit/<int:patient_id>/', views.edit, name='edit'),
    path('patients/delete/<int:patient_id>/', views.delete, name='delete'),
]
