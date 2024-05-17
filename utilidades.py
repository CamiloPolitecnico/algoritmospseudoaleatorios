class Utilidades:    
    def obtener_cifras_centrales(numero, x):
        num_str = str(numero)
        inicio = (len(num_str) - x) // 2
        cifras_centrales = num_str[inicio:inicio + x]
        if cifras_centrales[0] == '0':
            # Si la primera cifra es cero, tomar una cifra adicional a la derecha
            cifras_centrales = num_str[inicio:inicio + x + 1]
        return cifras_centrales
    
    def generar_array_pseudoaleatorio_no_congruencial(array_inicial, cifras):
        array_pseudoaleatorio = [0] * len(array_inicial)
        for x in range(len(array_inicial)):
            array_pseudoaleatorio[x] = array_inicial[x]/pow(10, int(cifras))
        return array_pseudoaleatorio
    
    def generar_array_pseudoaleatorio_congruencial(array_inicial, m):
        array_pseudoaleatorio = [0] * len(array_inicial)
        for x in range(len(array_inicial)):
            array_pseudoaleatorio[x] = array_inicial[x]/(m-1)
        return array_pseudoaleatorio
    
    def imprimir_respuesta(array):
        print("\nEl array de numeros pseudoaleatorios es:\n")
        print(array)
        print("----------------------------------------------")