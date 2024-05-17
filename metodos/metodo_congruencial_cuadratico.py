from utilidades import Utilidades
from validaciones import Validaciones

class MetodoCongruencialCuadratico:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.g = 0
        self.m = 0
        self.semilla = 0
        
    def generar_array_inicial(self, cant_aleatorios):
        array_inicial = [0] * cant_aleatorios
        for x in range(cant_aleatorios):
            if(x==0):
                array_inicial[x] = (self.a*(self.semilla**2) + self.b*self.semilla + self.c) % self.m
            else:
                array_inicial[x] = (self.a*(array_inicial[x-1]**2) + self.b*array_inicial[x-1] + self.c) % self.m
        return array_inicial
    
    def procesar_aleatorio(self):
        v = Validaciones()
        u = Utilidades
        print("\nAlgoritmo congruencial no lineal")
        self.g = v.validar_ingreso_constante("\nIngrese constante g, mayor a cero.")
        self.a = v.validar_ingreso_constante("\nIngrese constante a, mayor a cero. La constante a debe ser un numero par.", False, False, True)
        self.b = self.a + 1
        print("La constante b sera = ", self.b)
        self.c = v.validar_ingreso_constante("\nIngrese constante c, mayor a cero. La constante c debe ser un numero impar.", False, True)
        self.semilla = v.validar_ingreso_constante("\nIngrese semilla, mayor a cero.")
        self.m = pow(2, self.g) # calculo m
        
        print("\nIngrese cantidad de numeros aleatorios a generar")
        cant_aleatorios = int(input())
        
        array_inicial = self.generar_array_inicial(cant_aleatorios)
        array_pseudoaleatorios = u.generar_array_pseudoaleatorio_congruencial(array_inicial, self.m)
        u.imprimir_respuesta(array_pseudoaleatorios)