class Validaciones:
    global semilla
    
    def __init__(self):
        pass

    def solo_numeros(self, numero):
        return (numero.isdigit())
    
    def opcion_valida_menu(self, numero):
        opciones = [1, 2, 3, 4, 5, 6, 7]
        return (int(numero) in opciones)
    
    def numero_cifras_correcto(self, numero, cifras):
        numero_str = str(numero)
        return len(numero_str) >= cifras
    
    def validar_ingreso_semilla(self, cifras, mensaje):
        print(mensaje)
        flag = True
        while(flag):
            numeroInput = input()
            if(not(self.solo_numeros(numeroInput)) or not(self.numero_cifras_correcto(numeroInput, cifras))):
                print("Error, Opcion Invalida.")
                print(mensaje)
            else:
                semilla = int(numeroInput)
                flag = False
        return semilla
    
    def validar_ingreso_constante(self, mensaje):
        print(mensaje)
        flag = True
        global resultado
        while(flag):
            numeroInput = input()
            if(not(self.solo_numeros(numeroInput)) or int(numeroInput)<0):
                print("Error, Numero invalido.")
                print(mensaje)
            else:
                resultado = int(numeroInput)
                flag = False
        return resultado
    
    def validar_ingreso_constante_m(self, mensaje, array):
        print(mensaje)
        flag = True
        global resultado
        while(flag):
            numeroInput = input()
            mayor = all(int(numeroInput) > num for num in array)
            if(not(self.solo_numeros(numeroInput)) or not(mayor)) :
                print("Error, Numero invalido.")
                print(mensaje)
            else:
                resultado = int(numeroInput)
                flag = False
        return resultado