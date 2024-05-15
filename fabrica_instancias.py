from metodo_pseudo_aleatorio_cuadrado_medio import MetodoPseudoAleatorioCuadradoMedio

class FabricaInstancias:
    instancia = ""
    
    def obtener_instancia(option):
        match option:
            case 1:
                return MetodoPseudoAleatorioCuadradoMedio
    