#funcion que recibe una lista y devuelve el mayor
def devuelveMayor(lista):
    mayor = lista[0]
    for n in lista:
        if n > mayor:
            mayor = n
    return mayor#indentar fuera del for
milista = [2,4,6,8]
print(devuelveMayor(milista))

print(max(milista))#funcion que devuelve el mayor de la lista