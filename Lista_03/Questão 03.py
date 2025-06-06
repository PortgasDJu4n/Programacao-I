#--------Verificação de Turno-----------
print("Digite qual turno você estuda!")
turno = input("Matutino, Verpertino ou Noturno?: ")

#--Condicionais--
#Matutino
if turno == "Matutino" or turno == "matutino" or turno == "M" or turno == "m":
    print("Bom Dia!")
  
#Vespertino   
elif turno == "Vespertino" or turno == "vespertino" or turno == "V" or turno == "v":
    print("Boa Tarde!")
    
#Noturno    
elif turno == "Noturno" or turno == "noturno" or turno == "N" or turno == "n":
    print("Boa Noite!")
    
#Invalido
else:
    print("Valor Inválido!")

#Coloquei várias condicionais para caso o usuário digitar de outro jeito.
