# Crie um programa para calcular as notas obtidas pelo aluno do
# ensino médio, deverá mostrar mensagem para ser digitado a
# nota da 1ª, 2ª, 3ª e 4ª prova e a nota do 1º, 2º, 3º e 4º trabalho. Após deverá mostrar na tela a média obtida no 1º, 2º, 3º e 4º
# bimestre.
# E depois o total informado se o aluno foi aprovado, esta em
# recuperação ou foi reprovado sem recuperação.

print("programa para calcular notas de provas e trabalhos bimestrais")

p1 = float(input("qual a nota da prova do aluno no 1º Bimestre? (valor maximo 25) "))
t1 = float(input("qual a nota do trabalho do aluno 1º Bimestre? (valor maximo 25) "))

p2 = float(input("qual a nota da prova do aluno no 2º Bimestre? (valor maximo 25) "))
t2 = float(input("qual a nota do trabalho do aluno 2º Bimestre? (valor maximo 25) "))

p3 = float(input("qual a nota da prova do aluno no 3º Bimestre? (valor maximo 25) "))
t3 = float(input("qual a nota do trabalho do aluno 3º Bimestre? (valor maximo 25) "))

p4 = float(input("qual a nota da prova do aluno no 4º Bimestre? (valor maximo 25) "))
t4 = float(input("qual a nota do trabalho do aluno 4º Bimestre? (valor maximo 25) "))

b1 = (p1+t1) /2
b2 = (p2+t2) /2
b3 = (p3+t3) /2
b4 = (p4+t4) /2

print("a média do aluno no 1º Bimestre foi", b1)
print("a média do aluno no 2º Bimestre foi", b2)
print("a média do aluno no 3º Bimestre foi", b3)
print("a média do aluno no 4º Bimestre foi", b4)
resultado = b1 + b2 + b3 + b4

print("O resultado final do aluno foi: ", resultado)
if (resultado > 59 and resultado < 101):
    print("Aluno está Aprovado!")
elif (resultado >= 40 and resultado < 60):
    print("Aluno está em Recuperação!")
elif (resultado < 40 and resultado >= 0):
    print("Aluno está Reprovado!")
else:
    print("Confira os Valores Digitado, Valor invalido")
