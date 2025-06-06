#--------Investigação Criminal-----------
positivo = 0; negativo = 0;

print("Acabou de acontecer um crime...")
print("Quero que responda essas perguntas com sim ou não.")

#Primeira Pergunta
pq1 = input("Telefonou para a vítima?: ")
if pq1 == "sim" or pq1 == "Sim":
    positivo += 1
else:
    negativo += 1
    
#Segunda Pergunta
pq2 = input("Esteve no local do crime?: ")
if pq2 == "sim" or pq2 == "Sim":
    positivo += 1
else:
    negativo += 1
    
#Terceira Pergunta    
pq3 = input("Mora perto da vítima?: ")
if pq3 == "sim" or pq3 == "Sim":
    positivo += 1
else:
    negativo += 1

#Quarta Pergunta
pq4 = input("Devia para a vítima?: ")
if pq4 == "sim" or pq4 == "Sim":
    positivo += 1
else:
    negativo += 1
    
#Quinta Pergunta    
pq5 = input("Já trabalhou com a vítima?: ")
if pq5 == "sim" or pq5 == "Sim":
    positivo += 1
else:
    negativo += 1

#Afirmações e Negações
print(f"{positivo} afirmações e {negativo} negações.")

#Condicionais
if positivo == 2:
    print("Suspeita...")
    
elif positivo == 3 or positivo == 4:
    print("Cúmplice!")
    
elif positivo == 5:
    print("Assasino!")
    
else:
    print("Inocente, por enquanto...")
 
