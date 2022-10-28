# Crie um programa de calculadora que realiza as operações de
# soma, multiplicação, divisão e subtração, será perguntado ao
# usuário se deseja continuar com o uso da calculadora, enquanto ele digitar (“S” – Sim) o programa irá reiniciar a calculadora.

finalizar = "n"
while (finalizar != "s"):

    num1 = int(input("digite o primeiro número "))
    acao = str(input("qual será a operação? Digite o caractere(+, -, * ou /) "))
    num2 = int(input("digite o segundo número "))

    if (acao == "+"):
        print(num1, "+", num2, "=", num1 + num2)
        finalizar = input("deseja sair da calculadora? s/n? ")
    elif (acao == "-"):
        print(num1, "-", num2, "=", num1 - num2)
        finalizar = input("deseja sair da calculadora? s/n? ")
    elif (acao == "*"):
        print(num1, "*", num2, "=", num1 * num2)
        finalizar = input("deseja sair da calculadora? s/n? ")
    elif (acao == "/"):
        print(num1, "/", num2, "=", num1 / num2)
        finalizar = input("deseja sair da calculadora? s/n? ")
    else :
        print("operação invalida")
        finalizar = input("deseja sair da calculadora? s/n? ")

