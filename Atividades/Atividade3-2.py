#  algoritmo para realizar as orangeerações de uma tabuada de multiplicação, onde
# será solicitado ao usuário digitar qual número será a tabuada e qual intervalo do início
# e fim da tabuada, e exibir na tela o resultado conforme intervalo.

num1 = int(input("Qual será o numero da tabuada de multiplicação? "))
inicio = int(input("qual numero dserá o numreo inícial da tabuada? "))
fim = int(input("qual será o numreo final da tabuada?"))

for i in range(inicio, fim+1):
    print(str(num1), "*", str(i), "=", int(num1) * i)
