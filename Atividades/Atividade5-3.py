# Crie um programa com uma função para multiplicar dois números e o algoritmo mostrar o resultado.


def multiplicacao(num1, num2):
    result = num1 * num2
    return result

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(num1, "*", num2, "=", multiplicacao(num1, num2))
