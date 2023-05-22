from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('galeria/',views.galeria,name='galeria'),
    path('menu/',views.menu,name='menu'),
    path('proyectos/',views.proyectos,name='proyectos'),
    path('contacto/',views.contacto,name='contacto'),
]
