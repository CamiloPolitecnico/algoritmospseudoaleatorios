from utilidades import Utilidades
from validaciones import Validaciones

class MetodoCongruencialMultiplicativo:
    def __init__(self):
        self.a = 0
        self.k = 0
        self.g = 0
        self.m = 0
        self.semilla = 0
        
    def generar_array_inicial(self, cant_aleatorios):
        array_inicial = [0] * cant_aleatorios
        for x in range(cant_aleatorios):
            if(x==0):
                array_inicial[x] = ( (self.a*self.semilla)) % self.m
            else:
                array_inicial[x] = ( (self.a*array_inicial[x-1])) % self.m
        return array_inicial
    
    def procesar_aleatorio(self):
        v = Validaciones()
        u = Utilidades
        print("\nAlgoritmo congruencial multiplicativo")
        self.g = v.validar_ingreso_constante("\nIngrese constante g, mayor a cero.")
        self.k = v.validar_ingreso_constante("\nIngrese constante k, mayor a cero.")
        self.semilla = v.validar_ingreso_constante("\nIngrese semilla, mayor a cero. La semilla debe ser impar.", False, True)
        self.a = 5 + (8*self.k) #Calculo a
        self.m = pow(2, self.g) # calculo m
        
        print("\nIngrese cantidad de numeros aleatorios a generar")
        cant_aleatorios = int(input())
        array_inicial = self.generar_array_inicial(cant_aleatorios)
        array_pseudoaleatorios = u.generar_array_pseudoaleatorio_congruencial(array_inicial, self.m)
        u.imprimir_respuesta(array_pseudoaleatorios)
        
    
    