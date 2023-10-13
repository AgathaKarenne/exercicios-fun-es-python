#. O sindicato de trabalhadores de uma empresa sugere que o piso salarial da classe seja de R$ 1 800,00,
#propondo um aumento percentual fixo por cada ano dedicado ao trabalho. A expressão que corresponde à
#proposta salarial (s), em função do tempo de serviço (t), em anos, é s(t) = 1 800 . (1,03)t
# De acordo com a proposta do sindicato, o salário de um profissional dessa empresa com 2 anos de tempo de serviço será, em reais?

#sugestão de salario
piso_salarial = 1.800,00

# Tempo de serviço em anos
t = 2

# Expressão para o salário de acordo com a proposta do sindicato
salario = 1800 * (1.03)**t

print("O salário de um profissional com 2 anos de tempo de serviço é de R$ {:.2f}".format(salario))
