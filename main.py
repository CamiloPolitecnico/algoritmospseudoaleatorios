from fabrica_instancias import FabricaInstancias
from validaciones import Validaciones

class Main:
    def __init__(self):
        pass
    
    global v
    v = Validaciones()
    global m
    global f
    f = FabricaInstancias
    global option
    option = 0
    
    def mostrar_menu_principal(self):
        print("ALGORITMOS PSEUDOALEATORIOS")
        print("Digite la opcion del algoritmo pseudoaleatorio por favor:")
        print("1. No Congruencial cuadrados medios")
        print("2. No Congruencial productos medios")
        print("3. No Congruencial multiplicador constante")
        print("4. Congruencial lineal")
        print("5. Congruencial multiplicativo")
        print("6. Congruencial aditivo")
        print("7. Congruencial no lineal\n")
        
    def iniciar_programa(self):
        flag = True
        while(flag):
            self.mostrar_menu_principal()
            opcionMenu = input()
            if(not(v.solo_numeros(opcionMenu)) or not(v.opcion_valida_menu(opcionMenu))):
                print("Error, Opcion Invalida.")
            else:
                option=int(opcionMenu)
                flag = False
                
        instancia_metodo = f.obtener_instancia(option)
        instancia_metodo.procesar_aleatorio()
        
m = Main()
m.iniciar_programa()
        