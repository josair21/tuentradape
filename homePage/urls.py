from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.homePage, name="homePage"),
    path("comprar/", views.comprarPage, name="comprarPage"),
    path("validar/", views.validarPage, name="validarPage"),
]

urlpatterns += staticfiles_urlpatterns()