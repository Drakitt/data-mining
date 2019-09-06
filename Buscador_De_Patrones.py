class Buscador_De_Patrones:
    
    limiteA_superior = 0
    limiteB_superior = 0
    limiteC_superior = 0
    media = 0
    limiteC_inferior = 0
    limiteB_inferior = 0
    limiteA_inferior = 0

    def AjustarLimites(self, media, desviacion_media):
        self.limiteA_superior = media + desviacion_media * 3
        self.limiteB_superior = media + desviacion_media * 2
        self.limiteC_superior = media + desviacion_media
        self.media = media
        self.limiteC_inferior = media - desviacion_media
        self.limiteB_inferior = media - desviacion_media * 2
        self.limiteA_inferior = media - desviacion_media * 3
        return [
            self.limiteA_superior,
            self.limiteB_superior,
            self.limiteC_superior,
            self.media,
            self.limiteC_inferior,
            self.limiteB_inferior,
            self.limiteA_inferior]


    def BuscarPatron5(self, lista_datos, lista_fechas, i):
        if(i < len(lista_datos) - 2):
            #inferior
            if(lista_datos[i] > lista_datos[i+1] and lista_datos[i+1] > lista_datos[i+2] and lista_datos[i+1] < self.limiteB_inferior):
            
                print("Patron 5: " + str(lista_fechas[i]) + " - " + str(lista_fechas[i+2]))
            #superior
            if(lista_datos[i] < lista_datos[i+1] and lista_datos[i+1] < lista_datos[i+2] and lista_datos[i+1] > self.limiteB_inferior):
            
                print("Patron 5: " + str(lista_fechas[i]) + " - " + str(lista_fechas[i+2]))
            
        return True


    contador_Patron6=0
    aux=0
    def BuscarPatron6(self, lista_datos, lista_fechas, i):
        
        if(lista_datos[i] < self.limiteB_inferior and lista_datos[i] > self.limiteB_superior):
            self.contador_Patron6+=1
        elif(self.aux==0):
            self.aux=1
        elif(self.aux==1):
            self.contador_Patron6=0
            self.aux=0            
          
        if(self.contador_Patron6 >= 4):
            print("Patron 6: " + str(lista_fechas[i - 5]) + " - " + str(lista_fechas[i]))
            
        return True


    contador_Patron7 = 0
    def BuscarPatron7(self, lista_datos, lista_fechas, i):
        if(lista_datos[i] > self.limiteC_inferior and lista_datos[i] < self.limiteC_superior):
            self.contador_Patron7 += 1
        else:
            self.contador_Patron7 = 0

        if(self.contador_Patron7 >= 15):
            print("Patron 7: " + str(lista_fechas[i - 14]) + " - " + str(lista_fechas[i]))

        return True
    
    contador_Patron8 = 0
    def BuscarPatron8(self, lista_datos, lista_fechas, i):
        if(lista_datos[i] != self.limiteC_inferior and lista_datos[i] != self.limiteC_superior):
            self.contador_Patron8 += 1
        else:
            self.contador_Patron8 = 0

        if(self.contador_Patron8 == 8):
            print("Patron 8: " + str(lista_fechas[i - 7]) + " - " + str(lista_fechas[i]))

        return True