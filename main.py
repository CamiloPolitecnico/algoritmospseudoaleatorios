from fabrica_instancias import FabricaInstancias
from menus import Menus
from validaciones import Validaciones

class Main:
    global v
    v = Validaciones
    global m
    m = Menus
    global f
    f = FabricaInstancias
    global option
    option = 0
    
    def iniciar_programa():
        flag = True
        while(flag):
            m.mostrar_menu()
            opcionMenu = input()
            if(not(v.validar_solo_numeros(opcionMenu)) or not(v.validar_opcion_valida(opcionMenu))):
                print("Error, Opcion Invalida.")
            else:
                option=int(opcionMenu)
                flag = False
                
        instancia_metodo = f.obtener_instancia(option)
        instancia_metodo.ProcesarAleatorio()

Main.iniciar_programa()
        