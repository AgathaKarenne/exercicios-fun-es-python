#Um grupo de biólogos está estudando o desenvolvimento de uma determinada colônia de bactérias e
#descobriu que sob condições ideais, o número de bactérias pode ser encontrado através da expressão N(t)= 2000.2**0,5*t,
# sendo t em horas. Considerando essas condições, quanto tempo após o início da observação, o número de bactérias será igual a 8192000?


#numero de bacterias 
numero_bacterias = 8192000

#expressão que descreve o numero de bacterias 
def N(t):
    return  2000.2**(0,5*t)

#tempo em horas
t = 0

# Encontre o valor de t quando N(t) = bacterias_desejado
while N(t) < numero_bacterias:
    t += 1
    
#imprimir o numero de bacterias e o tempo
print("O número de bactérias será igual a 8192000 aproximadamente", t, "horas após o início da observação.")


