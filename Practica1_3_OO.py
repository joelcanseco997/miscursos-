import random
import numpy
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns
class TestLab:  ##Creacion de una clase.
    ## Declaracion de las constantes de la clase.
    TEMP_LIMITE_SUP = 250
    TEMP_LIMITE_INF = 85
    HUMEDAD_LIMITE_SUP = 101
    HUMEDAD_LIMITE_INF = 85
    ## Definicion de las propiedades de la clase.
    def __init__(self, int_o_float, limiteInf, limiteSup, limite_RH_inf, limite_RH_Sup, lista):
        self.int_o_float = int_o_float
        self.limiteInf = limiteInf
        self.limiteSup = limiteSup
        self.limite_RH_inf = limite_RH_inf
        self.limite_RH_Sup = limite_RH_Sup
        self.lista = lista
    ## Definicion del metodo es decir las operaciones a realizar 
    def GeneraNumAleatorio(self ):
        if( self.int_o_float =="int"):
            numeroAleatorio = random.randint(self.limiteInf, self.limiteSup)
        if( self.int_o_float == "float"):
            numeroAleatorio = random.uniform(self.limiteInf, self.limiteSup)

        return numeroAleatorio

    ListaDeNumero_int = []

    """def PrintLista(nombre_lista, lista):
    print(nombre_lista)
    print(lista)
ListaDeNumeroPart_int = []
ListaDeTemp_float = []
ListaDeHum_float = []

    for i in range(10):
    num_int = GeneraNumAleatorio("int", 10, 1000)
    num_float1 = GeneraNumAleatorio("float", 10.1, 199.9)
    num_float2 = GeneraNumAleatorio("float", 10.1, 99.9)
    ListaDeNumeroPart_int.append(num_int)
    ListaDeTemp_float.append(num_float1)
    ListaDeHum_float.append(num_float2)

PrintLista("int",ListaDeNumeroPart_int)
PrintLista("float", ListaDeTemp_float)
PrintLista("float", ListaDeHum_float)"""




