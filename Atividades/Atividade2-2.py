# programa que receba um numero digitado que será comparado se o numero digitado é maior que 10, igual a
# 10 ou menor que 10

num1 = int(input("digite um numero "))
if(int(num1) > 10):
    print("o numero " + str(num1) + " é maior que 10.")

elif(num1 < 10):
    print("o numero " + str(num1) + " é menor que 10.")

else:print("o numero " + str(num1) + " é igual á 10.")