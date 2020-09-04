from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="home"),
    # path('profile/', views.profile, name="profil"),
    path('enregisterement/', views.register, name='register'),
    path('addSchool/', views.registerSchool, name='addSchool'),
    path('addClass/', views.registerClass, name="addClass"),
    path('listEtudiant/', views.ListStudent, name='listeE'),
    path('updateEt/<int:student_id>', views.modifier, name="update"),
    path('supprimerEt/<student_id>/', views.delete, name="delete"),
    path('registerP/', views.registerProfil, name="registerP"),
    path('login/', views.connexion, name="login"),
    path('logout/', views.deconnexion, name="logout"),

]