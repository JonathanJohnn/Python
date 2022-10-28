#  algoritmo para realizar as orangeerações de uma tabuada de multiplicação, onde
# será solicitado ao usuário digitar qual número será a tabuada e qual intervalo do início
# e fim da tabuada, e exibir na tela o resultado conforme intervalo.
print("tabuada do numero desejado")

tabuada = int(input("Digite o inicio da tabuada: "))
inicio = int(input("Digite o inicio do intervalo da tabuada: "))
fim = int(input("Digite o fim do intervalo da tabuada: "))

for i in range(inicio, fim + 1):
    print("tabuada do numero", tabuada, "resultado: ", tabuada, "*", inicio, "=", tabuada * inicio)
    # print("tabuada resultado", tabuada * inicio)
    inicio = inicio + 1