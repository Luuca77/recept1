from django.urls import path
from . import views

urlpatterns = [
    path('', views.seznam_receptu, name='seznam'),
    path('recept/<int:pk>/', views.detail_receptu, name='detail'),
    path('pridat/', views.pridat_recept, name='pridat'),
    path('recept/<int:pk>/upravit/', views.upravit_recept, name='upravit'),
    path('recept/<int:pk>/smazat/', views.smazat_recept, name='smazat'),
    path('registrace/', views.registrace, name='registrace'),
    path('prihlaseni/', views.prihlaseni, name='prihlaseni'),
    path('odhlaseni/', views.odhlaseni, name='odhlaseni'),
]