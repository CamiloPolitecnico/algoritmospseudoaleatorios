class Utilidades:
    def obtener_cifras_centrales(numero, n):
        num_str = str(numero)
        total_cifras = len(num_str)
        inicio = (total_cifras - n) // 2
        cifras_centrales = num_str[inicio:inicio + n]
        return cifras_centrales
    
    def imprimir_respuesta(array):
        print("\nEl array de numeros pseudoaleatorios es:\n")
        print(array)
        print("----------------------------------------------")