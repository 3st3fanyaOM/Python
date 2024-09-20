#funcion que devuelve el numero de palabras de una frase introducida x usu
def contar():
    frase = "Hola que tal"
    palabras = frase.split()#crea una lista separada x espacios
    return len(palabras)

print(contar())