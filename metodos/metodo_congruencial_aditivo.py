from utilidades import Utilidades
from validaciones import Validaciones

class MetodoCongruencialAditivo:
    def __init__(self):
        self.semillas = []
        self.m = 0
        
    def generar_array_inicial(self, cant_aleatorios):
        aux_len = len(self.semillas)
        array_inicial = [0] * (cant_aleatorios + aux_len)
        
        for x in range(len(self.semillas)):
            array_inicial[x] = self.semillas[x]
            
        for x in range(aux_len, len(array_inicial)):
            num = (array_inicial[x-aux_len] + array_inicial[x-1]) % self.m
            array_inicial[x] = num
            
        return array_inicial
    
    def generar_array_pseudoaleatorio(self, array_inicial, cant_aleatorios):
        array_pseudoaleatorio = [0] * cant_aleatorios
        aux_len = len(self.semillas)
        for x in range(cant_aleatorios):
            array_pseudoaleatorio[x] = array_inicial[x + aux_len]/(self.m-1)
        return array_pseudoaleatorio
    
    def validar_positivos(self, numeros):
        for numero in numeros:
            if numero < 0:
                return False
        return True
    
    def validar_mayor(self):
        return all(self.m > num for num in self.semillas)
    
    def procesar_aleatorio(self):
        v = Validaciones()
        u = Utilidades
        print("Algoritmo congruencial aditivo")
        print("\nIngrese las semillas, una lista de números positivos separados por espacios.")
        entrada = input()
        self.semillas = [int(num) for num in entrada.split()]
    
        while(not(self.validar_positivos(self.semillas))):
            print("Error, uno de los numeros ingresados no es positivo")
            print("\nIngrese las semillas, una lista de números positivos separados por espacios.")
            entrada = input()
            self.semillas = [int(num) for num in entrada.split()]
        
        self.m = v.validar_ingreso_constante("\nIngrese constante m, m debe ser mayor a todos los números del array semilla.")
        while(not(self.validar_mayor())):
            print("Error, m debe ser mayor a todos los numeros del array semilla")
            self.m = v.validar_ingreso_constante("\nIngrese constante m, m debe ser mayor a todos los números del array semilla.")
        
        print("\nIngrese cantidad de numeros aleatorios a generar")
        cant_aleatorios = int(input())
        
        array_inicial = self.generar_array_inicial(cant_aleatorios)
        array_pseudoaleatorios = u.generar_array_pseudoaleatorio(array_inicial, cant_aleatorios)
        u.imprimir_respuesta(array_pseudoaleatorios)