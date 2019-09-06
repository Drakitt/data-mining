import numpy
import matplotlib.pyplot as plt

class Graficador:

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


    def GraficarA(self, lista_datos, lista_fechas):
        x = lista_fechas
        y = lista_datos

        def f(x):
            return x

        errorx=[]
        errory=[]
        posix=[]
        posiy=[]
        for j in range(len(y)):
            if(y[j]<=self.limiteC_inferior or y[j]>=self.limiteC_superior):
                errorx.append(x[j])
                errory.append(y[j])
            else:
                posix.append(x[j])
                posiy.append(y[j])

        plt.plot(x,y)
        plt.plot(errorx,errory,'o', color='r',markersize=2)
        plt.plot(posix,posiy,'o', color='g',markersize=2)

        plt.plot(x,[f(self.media) for i in x],label='LC')
        plt.plot(x,[f(self.limiteC_inferior) for i in x],label='LCS',color='y')
        plt.plot(x,[f(self.limiteC_superior) for i in x],label='LCI',color='y')

        plt.plot(x,[f(self.limiteB_inferior) for i in x],label='LCS',color='m')
        plt.plot(x,[f(self.limiteB_superior) for i in x],label='LCI',color='m')

        plt.plot(x,[f(self.limiteA_inferior) for i in x],label='LCS',color='r')
        plt.plot(x,[f(self.limiteA_superior) for i in x],label='LCI',color='r')

        #plt.legend(loc='upper left')
        plt.ylim(1000, 5000)
        plt.figure(figsize=(300,10))
        plt.show()
        return True


    def GraficarB(self, lista_datos, lista_fechas):
        return True