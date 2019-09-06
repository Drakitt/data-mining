import numpy
import statistics

class Operaciones_Matematicas:
    def SacarMedia(self, lista_datos):
        media = statistics.mean(lista_datos)
        print("Media: " + str(media))
        return media


    def SacarDesviacionMedia(self, lista_datos, media):
        cuadrados = []
        for dato in lista_datos:
            cuadrado = (dato - media)**2
            cuadrados.append(cuadrado)
        desviacion = (sum(cuadrados) / (len(lista_datos) - 1))**0.5
        print("Desviacion: " + str(desviacion))
        return desviacion