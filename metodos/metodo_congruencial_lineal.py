from utilidades import Utilidades
from validaciones import Validaciones

class MetodoCongruencialLineal:
    def __init__(self):
        self.a = 0
        self.k = 0
        self.g = 0
        self.c = 0
        self.m = 0
        self.semilla = 0
        
    def generar_array_inicial(self, cant_aleatorios):
        array_inicial = [0] * cant_aleatorios
        for x in range(cant_aleatorios):
            if(x == 0):
                num = ( (self.a*self.semilla) + self.c) % self.m
            else:
                num = ( (self.a*array_inicial[x-1]) + self.c) % self.m
            array_inicial[x] = num
        return array_inicial
    
    def procesar_aleatorio(self):
        v = Validaciones()
        u = Utilidades
        print("\nAlgoritmo congruencial lineal")
        self.g = v.validar_ingreso_constante("\nIngrese constante g, mayor a cero.")
        self.k = v.validar_ingreso_constante("\nIngrese constante k, mayor a cero.")
        self.c = v.validar_ingreso_constante("\nIngrese constante c, mayor a cero. La constante c debe ser un numero primo.", True)
        self.semilla = v.validar_ingreso_constante("\nIngrese semilla, mayor a cero.")
        self.a = 1 + (4*self.k) #Calculo a
        self.m = pow(2, self.g) # calculo m
        
        print("\nIngrese cantidad de numeros aleatorios a generar")
        cant_aleatorios = int(input())
        
        array_inicial = self.generar_array_inicial(cant_aleatorios)
        array_pseudoaleatorios = u.generar_array_pseudoaleatorio_congruencial(array_inicial, self.m)
        u.imprimir_respuesta(array_pseudoaleatorios)
        
    
    