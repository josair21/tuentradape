from django.shortcuts import render, redirect
from homePage.models   import Preguntas, Tipos
from .codigoValidacion import generaCodigoValidacion
from .codigoValidacion import almacenaCelularValidador


def homePage(request):
    return render(request, "homePage.html")

def comprarPage(request):
    preguntas = Preguntas.objects.all()
    entradas = Tipos.objects.all()
    datos = {
        'preguntas': preguntas,
        'entradas': entradas
    }

    if request.method == 'POST':
        if request.POST.get('boton') == 'sms':
            celular = request.POST.get('celular')
            print(celular)
            codigoValidacion=generaCodigoValidacion(6)
            almacenaCelularValidador(celular,codigoValidacion)

            datosSMS = {
                'preguntas': preguntas,
                'entradas':  entradas,
                'celular':   celular
                #'codigoValidacion':  codigoValidacion
            }
            
            return render(request, "comprarPage/comprarPage.html", datosSMS)

        elif request.POST.get('boton') == 'verificar':
            celular = request.POST.get('celular')
            print(celular)
            codigoValidacionIngresado = request.POST.get('codigo')
            print(codigoValidacionIngresado)

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
            return redirect("resumenPage")
    
    return render(request, "comprarPage/comprarPage.html", {'preguntas': preguntas,'entradas': entradas})

def validarPage(request):
    return render(request, "validarPage/validarPage.html")

def resumenPage(request):
    return render(request, "resumenPage/resumenPage.html")

def ticketsCompradosPage(request):
    return render(request, "ticketsCompradosPage/ticketsCompradosPage.html")