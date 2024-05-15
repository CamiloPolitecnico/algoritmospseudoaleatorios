class Validaciones:

    def validar_solo_numeros(numero):
        return (numero.isdigit())
    
    def validar_opcion_valida(numero):
        opciones = [1, 2, 3, 4, 5, 6, 7]
        return (int(numero) in opciones)