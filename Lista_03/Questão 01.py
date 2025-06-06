#--------Cálculo da Média-----------
#Entrada de dados
notas = input("Digite suas notas semestrais separada por virgula: ")
nota1, nota2, nota3 = notas.split(",")

#Conversão para Inteiro
nota1 = int(nota1); nota2 = int(nota2); nota3 = int(nota3)

#Cálculo da média
media = (nota1+nota2+nota3) / 3

#--Condicionais--
#Maior ou igual a 7
if media >= 7:
    print(f"sua média semestral foi {media}")
    print("Parabéns! Você foi aprovado!")
    
#Entre 6 e 4    
elif media < 7 and media >= 4:
    print(f"sua média semestral foi {media}")
    print("Você ficou de prova final :v.")
    
#Menor que 4    
else:
    print(f"sua média semestral foi {media}")
    print("Infelizmente, você foi reprovado.")
