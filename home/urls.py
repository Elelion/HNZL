from django.urls import path, include
from home.views import *

app_name = 'home'

urlpatterns = [
    path('', HomeListView.as_view(), name='index'),
    path('client_questions/', ClientQuestions.as_view(), name='client_questions'),
    path('client_results/', ClientResults.as_view(), name='client_results'),

    path('send_email_health_check/', send_email_health_check, name='send_email_health_check'),
    path('notification/<code>', notification, name='notification'),
]
