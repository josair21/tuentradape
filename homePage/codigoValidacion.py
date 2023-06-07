def generaCodigoValidacion(longitud):
    caracteres = string.ascii_letters + string.digits  # Letras mayúsculas, minúsculas y dígitos
    codigo = ''.join(random.choice(caracteres) for _ in range(longitud))
    return codigo