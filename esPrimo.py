#funcion que devuelve si n es primo
def esPrimo(num):
    for n in range(2,num):
        if num%n == 0:
            return False
    return True
print(esPrimo(5))
print(esPrimo(10))    