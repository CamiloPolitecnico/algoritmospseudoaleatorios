class Utilidades:    
    def obtener_cifras_centrales(numero, x):
        num_str = str(numero)
        inicio = (len(num_str) - x) // 2
        cifras_centrales = num_str[inicio:inicio + x]
        if cifras_centrales[0] == '0':
            # Si la primera cifra es cero, tomar una cifra adicional a la derecha
            cifras_centrales = num_str[inicio:inicio + x + 1]
        return cifras_centrales
    
    def imprimir_respuesta(array):
        print("\nEl array de numeros pseudoaleatorios es:\n")
        print(array)
        print("----------------------------------------------")