# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
# para o sindicato, mostre todos os descontos, mostre o salário bruto e o líquido.

valor = float(input("quantos você ganha por hora?: "))
horas = float(input("quantas horas você trabalha?: "))
mes = horas*30
salario = valor*mes
print("esse é o seu salario bruto: ", salario)
inss2 = (salario - (8/100) * salario)
print("esse é seu salario com o INSS: ", inss2)
sind = (salario - (5/100) * salario)
print ("esse é o seu salario com o Sindicato: ", sind)
imposto = (salario - (11/100)*salario)
print("esse é se salatio com o imposto: ", imposto)
inss = (imposto - (8/100) * salario)
print("esse é seu salario com imposto e INSS: ", inss)
sind = (inss - (5/100) * salario)
print ("esse é o seu salario liquido: ", sind)
