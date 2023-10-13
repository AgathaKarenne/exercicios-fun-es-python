#1. A água é essencial para a vida e está presente na constituição de todos os alimentos. Em regiões com
#escassez de água, é comum a utilização de cisternas para a captação e armazenamento da água da chuva.
#Ao esvaziar um tanque contendo água da chuva, a expressão  v(t) = - 1/43200*t² + 3 representa o volume (em m3)
# de água presente no tanque no instante t (em minutos). Qual é o tempo, em
#horas, necessário para que o tanque seja esvaziado? faça uma representação grafica por python.

import numpy as np
import matplotlib.pyplot as plot

# Função para o volume da água no tanque
def v(t):
    return - 1/43200*t**2 + 3 

#tempo amostrado uniformemente em intervalos de 360 minutos 
t = np.linspace(0, 360, 100)

#volume deve receber v(t)
volume = v(t)

# sso criará um gráfico mostrando como o volume da água diminui ao longo do tempo, com a água ficando completamente esgotada em aproximadamente 6 horas.
plot.plot(t, volume)
plot.xlabel("Tempo (minutos)")
plot.ylabel("Volume (m³)")
plot.title("Esvaziamento do Tanque de Água da Chuva")
plot.grid(True)
plot.show()


