from utilidades import Utilidades
from validaciones import Validaciones

class MetodoMultiplicadorConstante:
    def __init__(self):
       self.semilla = 0
       self.constante = 0
    
    def generar_array_inicial(self, num_cifras, cant_aleatorios):
        array_inicial = [0] * cant_aleatorios
        u = Utilidades
        array_inicial[0]= self.semilla
        for x in range(1, cant_aleatorios):
            num_mult = array_inicial[x-1] * self.constante
            cifras_centrales = u.obtener_cifras_centrales(num_mult, num_cifras)
            array_inicial[x] = int(cifras_centrales)
        return array_inicial
    
    def generar_array_pseudoaleatorio(self, array_inicial, cifras):
        array_pseudoaleatorio = [0] * len(array_inicial)
        for x in range(len(array_inicial)):
            array_pseudoaleatorio[x] = array_inicial[x]/pow(10, int(cifras))
        return array_pseudoaleatorio
    
    def procesar_aleatorio(self):
        v = Validaciones()
        u = Utilidades
        
        print("\nMetodo multiplicador constante")
        
        self.constante = v.validar_ingreso_semilla(4, "Por favor ingrese constante, recuerde numero positivo de 4 cifras o mayor")
        cifras = len(str(self.constante))
        
        while(self.constante>=self.semilla):
            self.semilla = v.validar_ingreso_semilla(cifras, "Por favor ingrese semilla, recuerde numero positivo > a constante")
        
        print("\nIngrese cantidad de numeros aleatorios a generar")
        cant_aleatorios = int(input())
        cifras = len(str(self.semilla))
        array_inicial = self.generar_array_inicial(cifras, cant_aleatorios)
        array_pseudoaleatorios = self.generar_array_pseudoaleatorio(array_inicial, cifras)
        u.imprimir_respuesta(array_pseudoaleatorios)