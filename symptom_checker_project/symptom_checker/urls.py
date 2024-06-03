from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('check_symptoms/', views.check_symptoms, name='check_symptoms'),
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
]