# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
# para o sindicato, mostre todos os descontos, mostre o salário bruto e o líquido.

valor = float(input("digite o valor de horas trabalhadas: "))
horas = float(input("Digite o numero de horas trabalhads no mês: "))

salariobruto = valor * horas
inss = salariobruto * 0.08
ir = salariobruto * 0.11
sindicato = salariobruto * 0.05

salarioliquido = salariobruto - inss - ir - sindicato

print("salario bruto: R$  ", round(salariobruto, 2))
print("desconto INSS: R$ ", round(inss, 2))
print("desconto Imposto de Renda: R$ ", round(ir, 2))
print("desconto sindicato: R$ ", round(sindicato, 2))
print("esse é o seu salario: R$ ", round(salarioliquido, 2))