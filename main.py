from datetime import datetime

from Generador_De_Datos import Generador_De_Datos
from Buscador_De_Patrones import Buscador_De_Patrones
from Operaciones_Matematicas import Operaciones_Matematicas
from Graficador import Graficador

# Se definen los parametros
cantidad_de_datos = 500
valor_minimo = 2000
valor_maximo = 4000
fecha_inicio = datetime(2019,8,1,0,0,0)

# Se generan los datos
generador = Generador_De_Datos()

lista_datos = generador.GenerarListaDatos(cantidad_de_datos, valor_minimo, valor_maximo)
lista_fechas = generador.GenerarListaFechas(cantidad_de_datos, fecha_inicio)

# Se sacan la media y la desviacion
operaciones = Operaciones_Matematicas()

media = operaciones.SacarMedia(lista_datos)
desviacion_media = operaciones.SacarDesviacionMedia(lista_datos, media)

# Se buscan los patrones
buscador = Buscador_De_Patrones()

buscador.AjustarLimites(media, desviacion_media)

for i in range(len(lista_datos)):
    buscador.BuscarPatron5(lista_datos, lista_fechas, i)
    buscador.BuscarPatron6(lista_datos, lista_fechas, i)
    buscador.BuscarPatron7(lista_datos, lista_fechas, i)
    buscador.BuscarPatron8(lista_datos, lista_fechas, i)

# Se grafican los datos
graficador = Graficador()

graficador.AjustarLimites(media, desviacion_media)

graficador.GraficarA(lista_datos, lista_fechas)
graficador.GraficarB(lista_datos, lista_fechas)