class Persona:
    def __init__(self, nombre, edad, genero): #constructor del obj
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        if edad >=18:#funcion que determina si es mayor de edad
            self.mayorEdad = True
        else:
            self.mayorEdad = False

    def imprimirDatos(self): #funcion para imprimir una persona
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nGenero: {self.genero}\nMayor de edad: {self.mayorEdad}") #todo en la misma línea

persona1 = Persona("luis",20,"M")#indentar al principio para separar de la clase
persona1.imprimirDatos()
        
