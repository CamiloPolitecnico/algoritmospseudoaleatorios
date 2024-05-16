from utilidades import Utilidades
from validaciones import Validaciones

class MetodoCongruencialLineal:
    def __init__(self):
        self.a = 0
        self.c = 0
        self.m = 0
        self.semilla = 0
        
    def generar_array_inicial(self, cant_aleatorios):
        array_inicial = [0] * cant_aleatorios
        array_inicial[0]= self.semilla
        for x in range(1, cant_aleatorios):
            num = ( (self.a*array_inicial[x-1]) + self.c) % self.m
            array_inicial[x] = num
        return array_inicial
    
    def generar_array_pseudoaleatorio(self, array_inicial):
        array_pseudoaleatorio = [0] * len(array_inicial)
        for x in range(len(array_inicial)):
            array_pseudoaleatorio[x] = array_inicial[x]/self.m
        return array_pseudoaleatorio
    
    def procesar_aleatorio(self):
        v = Validaciones()
        u = Utilidades
        print("Algoritmo congruencial lineal\n")
        self.a = v.validar_ingreso_constante("Ingrese constante a, mayor a cero\n")
        self.c = v.validar_ingreso_constante("Ingrese constante c, mayor a cero\n")
        self.semilla = v.validar_ingreso_constante("Ingrese semilla, mayor a cero\n")
        self.m = v.validar_ingreso_constante_m("Ingrese constante m, debe ser mayor a la semilla, a y c\n", [self.a, self.c, self.semilla])
        
        print("\nIngrese cantidad de numeros aleatorios a generar")
        cant_aleatorios = int(input())
        array_inicial = self.generar_array_inicial(cant_aleatorios)
        array_pseudoaleatorios = self.generar_array_pseudoaleatorio(array_inicial)
        u.imprimir_respuesta(array_pseudoaleatorios)
        
    
    