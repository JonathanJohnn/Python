# Faça um programa que calcule o fatorial de um número, é obrigatório o uso de função recursiva para o calculo fatorial.

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

n = int(input("digite um número: "))
print(" o fatorial de ", n,"é: ", fatorial(n))