from utilidades import Utilidades
from validaciones import Validaciones

class MetodoPseudoAleatorioCuadradoMedio:
    def __init__(self):
        pass
        
    def generar_array_inicial(self, num_cifras, cant_aleatorios):
        array_inicial = [0] * cant_aleatorios
        u = Utilidades
        for x in range(cant_aleatorios):
            if(x == 0):
                array_inicial[x]= semilla
            else:
                num_cuadrado = pow(array_inicial[x-1], 2)
                cifras_centrales = u.obtener_cifras_centrales(num_cuadrado, num_cifras)
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
        global semilla
        print("\nMetodo de los cruadrados medios")
        
        semilla = v.validar_ingreso_semilla(4, "Por favor ingrese semilla, recuerde numero positivo de 4 cifras o mayor")
        
        print("\nIngrese cantidad de numeros aleatorios a generar")
        cant_aleatorios = int(input())
        cifras = len(str(semilla))
        
        array_inicial = self.generar_array_inicial(cifras, cant_aleatorios)
        array_pseudoaleatorios = self.generar_array_pseudoaleatorio(array_inicial, cifras)
        u.imprimir_respuesta(array_pseudoaleatorios)
    