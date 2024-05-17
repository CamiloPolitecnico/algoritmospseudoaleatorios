from metodos.metodo_congruencial_aditivo import MetodoCongruencialAditivo
from metodos.metodo_congruencial_cuadratico import MetodoCongruencialCuadratico
from metodos.metodo_congruencial_lineal import MetodoCongruencialLineal
from metodos.metodo_congruencial_multiplicativo import MetodoCongruencialMultiplicativo
from metodos.metodo_multiplicador_constante import MetodoMultiplicadorConstante
from metodos.metodo_productos_medios import MetodoProductosMedios
from metodos.metodo_pseudo_aleatorio_cuadrado_medio import MetodoPseudoAleatorioCuadradoMedio

class FabricaInstancias:

    def obtener_instancia(option):
        match option:
            case 1:
                return MetodoPseudoAleatorioCuadradoMedio()
            case 2:
                return MetodoProductosMedios()
            case 3:
                return MetodoMultiplicadorConstante()
            case 4:
                return MetodoCongruencialLineal()
            case 5:
                return MetodoCongruencialMultiplicativo()
            case 6:
                return MetodoCongruencialAditivo()
            case 7:
                return MetodoCongruencialCuadratico()
    