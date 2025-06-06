#--------Maior Número-----------
#Entrada de dados
print("Vamos verificar qual o maior número entre 3!")
numeros = input("Digite os 3 números separados por virgula: ")

#Conversão dados para Int
num1, num2, num3 = numeros.split(",") #Separação em var
num1 = int(num1); num2 = int(num2); num3 = int(num3) 

#Primeiro como maior
if num1 > num2 and num1 > num3:
    print(f"O maior número é: {num1}")

#Segundo como maior
elif num2 > num1 and num2 > num3:
    print(f"O maior número é: {num2}")

#Números iguais
elif num1 == num2 and num2 == num3:
    print(f"Todos os números são iguais: {num3}")
    
#Terceiro como maior    
else:
    print(f"O maior número é: {num3}")
