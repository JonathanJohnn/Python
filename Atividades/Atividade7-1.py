# Faça um Programa que leia dois vetores com 10 posições cada e receba números inteiros. Gere um terceiro vetor de 20
# elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. Mostre ao final
# os três vetores.

vetor1 = [0,0,0,0,0,0,0,0,0,0]
vetor2 = [0,0,0,0,0,0,0,0,0,0]
vetor3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    vetor1[i] = int(input("Digite um número para o primeiro vetor: "))

for i in range(10):
    vetor2[i] = int(input("Digite um número para o segundo vetor: "))

print("esse é o primeiro vetor: ", vetor1)
print("esse é o segundo vetor: ", vetor2)
vetor3 = vetor1 + vetor2
vetor3[::2] = vetor1
vetor3[1::2] = vetor2
print("a lista intercalada é : ", vetor3)
