from utilidades import Utilidades
from validaciones import Validaciones

class MetodoMultiplicadorConstante:
    def __init__(self):
       self.semilla = 0
       self.constante = 0
    
    def generar_array_inicial(self, num_cifras, cant_aleatorios):
        array_inicial = [0] * cant_aleatorios
        u = Utilidades
        for x in range(cant_aleatorios):
            if(x==0):
                num_mult = self.semilla * self.constante
            else:
                num_mult = array_inicial[x-1] * self.constante
            cifras_centrales = u.obtener_cifras_centrales(num_mult, num_cifras)
            array_inicial[x] = int(cifras_centrales)
        return array_inicial
    
    def procesar_aleatorio(self):
        v = Validaciones()
        u = Utilidades
        
        print("\Algoritmo no congruencial multiplicador constante")
        
        self.constante = v.validar_ingreso_semilla(4, "Por favor ingrese constante, recuerde numero positivo de 4 cifras o mayor")
        cifras = len(str(self.constante))
        
        while(self.constante>=self.semilla):
            self.semilla = v.validar_ingreso_semilla(cifras, "Por favor ingrese semilla, recuerde numero positivo > a constante")
        
        print("\nIngrese cantidad de numeros aleatorios a generar")
        cant_aleatorios = int(input())
        cifras = len(str(self.semilla))
        array_inicial = self.generar_array_inicial(cifras, cant_aleatorios)
        array_pseudoaleatorios = u.generar_array_pseudoaleatorio_no_congruencial(array_inicial, cifras)
        u.imprimir_respuesta(array_pseudoaleatorios)