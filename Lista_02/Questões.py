#Questão 01.
nomes = input("Digite os nomes que desejar: ")
lista = nomes.split(" ")
print(lista)

#Questão 02.
numeros = input("Digite números separados por vírgula: ")
lista = numeros.split(",")

lista = [int(numeros) for numeros in lista]

print(lista)

#Questão 03
data = input("Digite uma data no formato dd/mm/aaaa: ")
dia,mes,ano = data.split("/")

print(f"você digitou o dia {dia}, do mês {mes}, do ano de {ano}")
