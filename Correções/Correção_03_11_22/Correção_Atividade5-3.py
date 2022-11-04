# Crie um programa com uma função para multiplicar dois números e o algoritmo mostrar o resultado.

def multipicacao(n1, n2):
    result = n1 * n2
    return result

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print("resultado da multiplicação é: ", round(multipicacao(n1, n2), 2))
