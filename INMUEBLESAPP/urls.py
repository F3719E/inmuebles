from django.urls import path
from . import views




urlpatterns = [
    path('',views.index),
    # path('bienvenido/', views.bienvenido),
    # path('contacto/', views.contacto),
]



