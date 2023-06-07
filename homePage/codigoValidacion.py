import random
import string
from .models import codigosCelularValidacion

def generaCodigoValidacion(longitud):
    existe   = True
    intentos = 0 
    while (existe == True and intentos<10):
        intentos   = intentos + 1
        caracteres = string.ascii_letters + string.digits  # Letras mayúsculas, minúsculas y dígitos
        codigo     = ''.join(random.choice(caracteres) for _ in range(longitud))
        #print("Codigo generado = "+codigo)
        #codigo     = "963741"
        #print("Comparacion forzada con uno igual")
        if codigosCelularValidacion.objects.filter(codigovalidacion=codigo).exists():
            existe = True
            #print("Paso por True en generaCodigoValidacion. Intento:"+str(intentos))
        else:
            existe = False

    return codigo

def almacenaCelularValidador(celular,codigoValidacion):
    registro = codigosCelularValidacion()
    
    registro.celular          = celular
    registro.codigovalidacion = codigoValidacion
    registro.save()
    return