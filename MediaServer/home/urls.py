from django.urls import path
from . import views

urlpatterns =[
    path('home/',views.homepage,name = 'homepage'),
    path('',views.firstpage,name = 'firstpage'),
    path('toggle-theme/', views.toggle_theme, name='toggle_theme'),
    ]