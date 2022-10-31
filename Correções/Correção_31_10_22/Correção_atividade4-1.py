# Crie um programa para calcular as notas obtidas pelo aluno do
# ensino médio, deverá mostrar mensagem para ser digitado a
# nota do 1º, 2º, 3º e 4º bimestre. Após deverá mostrar na tela se o aluno foi aprovado, se está em recuperação ou foi reprovado
# sem chance de recuperação.
# Lembrando que cada bimestre vale 25 pontos num total anual de 100 pontos.

print("programa para calcular notas bimestrais")

b1 = float(input("qual nota o aluno alcançou no 1º Bimestre? (valor maximo 25) "))
b2 = float(input("qual nota o aluno alcançou no 2º Bimestre? (valor maximo 25) "))
b3 = float(input("qual nota o aluno alcançou no 3º Bimestre? (valor maximo 25) "))
b4 = float(input("qual nota o aluno alcançou no 4º Bimestre? (valor maximo 25) "))

resultado = b1 + b2 + b3 + b4
print("O resultado final do aluno foi: ")
if (resultado > 59 and resultado < 101):
    print("Aluno está Aprovado!")
elif (resultado >= 40 and resultado < 60):
    print("Aluno está em Recuperação!")
elif (resultado < 40 and resultado >= 0):
    print("Aluno está Reprovado!")
else:
    print("Confira os Valores Digitado, Valor invalido")
