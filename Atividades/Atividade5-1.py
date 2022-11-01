# Faça um Programa que leia em um vetor de 10 caracteres (letras ) e diga quantas consoantes foram lidas.
# Mostre as consoantes.

lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
num = 0

for i in range(10):
    lista[i] = str(input("digite uma letra: ")).upper()

for i in range(10):
    if lista[i] != "A" and lista[i] != "E" and lista[i] != "I" and lista[i] != "O" and lista[i] != "U":
        print(lista[i])
        num = num + 1

print(num, "consoantesforam digitadas")
