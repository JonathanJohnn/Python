# Crie um programa para calcular as notas obtidas pelo aluno do
# ensino médio, deverá mostrar mensagem para ser digitado a
# nota da 1ª, 2ª, 3ª e 4ª prova e a nota do 1º, 2º, 3º e 4º trabalho. Após deverá mostrar na tela a média obtida no 1º, 2º, 3º e 4º
# bimestre.
# E depois o total informado se o aluno foi aprovado, esta em
# recuperação ou foi reprovado sem recuperação.

notap1 = float(input("qual a nota da prova do aluno no 1º Bimestre? "))
notat1 = float(input("qual a nota do trabalho do aluno no 1º Bimestre? "))

notap2 = float(input("qual a nota da prova do aluno no 2º Bimestre? "))
notat2 = float(input("qual a nota do trabalho do aluno no 2º Bimestre? "))

notap3 = float(input("qual a nota da prova do aluno no 3º Bimestre? "))
notat3 = float(input("qual a nota do trabalho do aluno no 3º Bimestre? "))

notap4 = float(input("qual a nota da prova do aluno no 4º Bimestre? "))
notat4 = float(input("qual a nota do trabalho do aluno no 4º Bimestre? "))

notab1 = notap1 + notat1
notab2 = notap2 + notat2
notab3 = notap3 + notat3
notab4 = notap4 + notat4
notafinal = (notab1 + notab2 + notab3 + notab4)

if(notafinal >= 60 <= 100):
        print("Aluno Aprovado!")
elif(notafinal >= 40 <= 60 ):
        print("Aluno em Recuperação!")
elif(notafinal < 40 >= 0):
        print("Aluno Reprovado!(sem chance de recuperação)")

print("a média do aluno no 1º Bimestre foi", notab1/2)
print("a média do aluno no 2º Bimestre foi", notab2/2)
print("a média do aluno no 3º Bimestre foi", notab3/2)
print("a média do aluno no 4º Bimestre foi", notab4/2)
