from utilidades import Utilidades
from validaciones import Validaciones

class MetodoPseudoAleatorioCuadradoMedio:
    def __init__(self):
        self.semilla = 0
        
    def generar_array_inicial(self, num_cifras, cant_aleatorios):
        array_inicial = [0] * cant_aleatorios
        u = Utilidades
        for x in range(cant_aleatorios):
            if(x == 0):
                num_cuadrado = pow(self.semilla, 2)
            else:
                num_cuadrado = pow(array_inicial[x-1], 2)
            cifras_centrales = u.obtener_cifras_centrales(num_cuadrado, num_cifras)
            array_inicial[x] = int(cifras_centrales)
        return array_inicial
    
    def procesar_aleatorio(self):
        v = Validaciones()
        u = Utilidades
        print("\nAlgoritmo no congruencial cruadrados medios")
        
        self.semilla = v.validar_ingreso_semilla(4, "Por favor ingrese semilla, recuerde numero positivo de 4 cifras o mayor")
        
        print("\nIngrese cantidad de numeros aleatorios a generar")
        cant_aleatorios = int(input())
        cifras = len(str(self.semilla))
        
        array_inicial = self.generar_array_inicial(cifras, cant_aleatorios)
        array_pseudoaleatorios = u.generar_array_pseudoaleatorio_no_congruencial(array_inicial, cifras)
        u.imprimir_respuesta(array_pseudoaleatorios)
    