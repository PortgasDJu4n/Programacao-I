#Questão 03 - Cálculo do Salário Mensal

print("   *Calculo do Salário Mensal*")

#Entrada dos Dados
money = float(input("Quanto você ganha por hora:"))
hour = int(input("Quantidade de horas trabalhada por dia:"))
#Acho que é mais facil para o usuário saber a quantidade de horas diarias.

#Cálculo da renda
renda = money * hour * 22 #22 dias utéis no mês

#Exibição da renda mensal
print(f"Sua renda mensal é aproximadamente R${renda}")
