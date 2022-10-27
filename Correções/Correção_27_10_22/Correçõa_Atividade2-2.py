# programa que receba um numero digitado que será comparado se o numero digitado é maior que 10, igual a
# 10 ou menor que 10

num1 = int(input("digite um numero "))
#Não sera tratdo erro de digitação do usuario
if(int(num1) > 10):
    print("o numero " + str(num1) + " é maior que o numero secreto.")

elif(num1 < 10):
    print("o numero " + str(num1) + " é menor que o numero secreto.")

else:
    print("Acertou o numero secreto")