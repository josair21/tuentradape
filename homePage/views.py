from django.shortcuts import render
from homePage.models import Preguntas

def homePage(request):
    return render(request, "homePage.html")

def comprarPage(request):
    #preguntas = Preguntas.object.all()
    return render(request, "comprarPage/comprarPage.html")

def validarPage(request):
    return render(request, "validarPage/validarPage.html")