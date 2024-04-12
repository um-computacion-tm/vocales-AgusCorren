from test_contador_vocales import contar_vocales

activado = True
while activado==True:
    palabra = input('Ingrese palabra: ')
    print(contar_vocales(palabra))
    
    seguir = input('¿Desea continuar? Si/No: ')
    seguir = seguir.lower()
    if seguir == "si":
        continue
    else:
        activado = False