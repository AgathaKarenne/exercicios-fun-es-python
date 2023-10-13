#Para evitar uma epidemia, a Secretaria de Saúde de uma cidade dedetizou todos os bairros, de modo a
#evitar a proliferação do mosquito da dengue. Sabe-se que o número f de infectados é dado pela função f(t)= - 2t2 + 120t 
# (em que t é expresso em dia e t = 0 é o dia anterior à primeira infecção) e que tal expressão é
#válida para os 60 primeiros dias da epidemia. A Secretaria de Saúde decidiu que uma segunda dedetização
#deveria ser feita no dia em que o número de infectados chegasse à marca de 1 600 pessoas, e uma segunda
#dedetização precisou acontecer. A segunda dedetização começou no dia?

# Função que descreve o número de infectados ao longo do tempo
def f(t):    
    return  - 2 * t**2 + 120*t

#o número de infectados chegasse à marca de 1 600 pessoas, e uma segunda
#dedetização precisou acontecer
marca_numero_infectados = 1600

#agora iremos encontrar o valor do tempo quando ocorreu a marca de infectados
t = 0
#o tempo será iniciado com 0

#repetição do valor de infectados
while f(t) < marca_numero_infectados: 
    t+= 1

#imprimir o dia da segunda dedetização
print("A segunda dedetização começou no dia:", t)



