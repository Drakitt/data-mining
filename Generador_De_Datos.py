import numpy
import datetime

class Generador_De_Datos:

    def GenerarListaDatos(self, cantidad_de_datos, valor_minimo, valor_maximo):
        lista_datos = numpy.random.randint(valor_minimo, valor_maximo + 1, cantidad_de_datos)
        print("Datos Generados: " + str(len(lista_datos)))
        return lista_datos

    def GenerarListaFechas(self, cantidad_de_datos, fecha_inicio):
        fin = fecha_inicio + datetime.timedelta(seconds=cantidad_de_datos - 1)
        lista_fechas = [fecha_inicio + datetime.timedelta(seconds=s) for s in range((fin - fecha_inicio).seconds + 1)] 
        print("Fechas Generadas: " + str(len(lista_fechas)))
        return lista_fechas