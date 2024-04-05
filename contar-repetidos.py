def obtener_fi(lista_de_datos):
    lista_de_datos.sort()
    fi = {}
    for i in lista_de_datos:
        if i in fi:
            fi[i] += 1
        else:
            fi[i] = 1
    return fi