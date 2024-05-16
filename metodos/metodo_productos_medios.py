from utilidades import Utilidades
from validaciones import Validaciones


class MetodoProductosMedios:
    def __init__(self):
       self.semilla1 = 0
       self.semilla2 = 0
    
    def generar_array_inicial(self, num_cifras, cant_aleatorios):
        array_inicial = [0] * cant_aleatorios
        u = Utilidades
        array_inicial[0]= self.semilla1
        array_inicial[1]= self.semilla2
        for x in range(2, cant_aleatorios):
            num_mult = array_inicial[x-1] * array_inicial[x-2]
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
        
        print("\nMetodo de los cruadrados medios")
        
        self.semilla1 = v.validar_ingreso_semilla(4, "Por favor ingrese semilla 1, recuerde numero positivo de 4 cifras o mayor")
        self.semilla2 = v.validar_ingreso_semilla(4, "Por favor ingrese semilla 2, recuerde numero positivo de 4 cifras o mayor")
        
        print("\nIngrese cantidad de numeros aleatorios a generar")
        cant_aleatorios = int(input())
        cifras = len(str(self.semilla1))
        array_inicial = self.generar_array_inicial(cifras, cant_aleatorios)
        array_pseudoaleatorios = self.generar_array_pseudoaleatorio(array_inicial, cifras)
        u.imprimir_respuesta(array_pseudoaleatorios)