from django.urls import path, include

# При использовании from . import views внутри модуля или пакета означает, что вы
# импортируете модуль views из текущего пакета или из текущей директории. Символ .
# в данном случае представляет текущий пакет или текущую директорию.
from . import views

# from .views import AboutView, ContactsView

app_name = 'authorization'

urlpatterns = [
    # главная страница (вызываем через ф-цию)
    # path('', IndexView.as_view(), name='home'),
    path('login/', views.index, name='login'),
    path('logout/', views.logout, name='logout'),

    # path('about', AboutView.as_view(), name='about'),

    # path('contacts', ContactsView.as_view(), name='contacts'),
]
