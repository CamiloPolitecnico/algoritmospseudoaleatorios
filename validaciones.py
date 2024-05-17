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
    
    def validar_ingreso_constante(self, mensaje, primo = False, impar = False, par = False):
        print(mensaje)
        flag = True
        global resultado
        while(flag):
            numeroInput = input()
            if(not(self.solo_numeros(numeroInput)) or int(numeroInput)<0):
                print("Error, Numero invalido.")
                print(mensaje)
            elif(primo and not(self.es_primo(numeroInput))):
                print("Error, Numero invalido. No es primo")
                print(mensaje)
            elif(impar and not(self.es_impar(numeroInput))):
                print("Error, Numero invalido. Debe ser impar")
                print(mensaje)
            elif(par and self.es_impar(numeroInput)):
                print("Error, Numero invalido. Debe ser par")
                print(mensaje)
            else:
                resultado = int(numeroInput)
                flag = False
        return resultado
    
    def es_primo(self, numero):
        if int(numero) <= 1:
            return False
        if int(numero) == 2:
            return True
        if int(numero) % 2 == 0:
            return False
        for i in range(3, int(int(numero)**0.5) + 1, 2):
            if int(numero) % i == 0:
                return False
        return True
    
    def es_impar(self, numero):
        if int(numero) % 2 != 0:
            return True
        else:
            return False