from django.shortcuts import render
from homePage.models import Preguntas

def homePage(request):
    return render(request, "homePage.html")

def comprarPage(request):
    
    if request.method == 'POST':
        if request.POST.get('boton') == 'sms':
            celular = request.POST.get('celular')
            print(celular)
            CodigoValidacion=generaCodigoValidacion()
            almacenaCelularValidador(CodigoValidacion)

        elif request.POST.get('boton') == 'verificar':
            print(request.POST.get('celular'))
            print(request.POST.get('codigo'))
        elif request.POST.get('boton') == 'comprar':
            print(request.POST.get('celular'))
            print(request.POST.get('codigo'))
            print(request.POST.get('pin'))
            print(request.POST.get('medioPago'))
            print(request.POST.get('nombre'))
            print(request.POST.get('correo'))
            print(request.POST.get('dni'))
            print(request.POST.get('pregunta1'))
            print(request.POST.get('pregunta2'))
    preguntas = Preguntas.objects.all()
    return render(request, "comprarPage/comprarPage.html", {'preguntas': preguntas})

def validarPage(request):
    return render(request, "validarPage/validarPage.html")

def resumenPage(request):
    return render(request, "resumenPage/resumenPage.html")

def ticketsCompradosPage(request):
    return render(request, "ticketsCompradosPage/ticketsCompradosPage.html")