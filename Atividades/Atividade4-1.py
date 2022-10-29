# Crie um programa para calcular as notas obtidas pelo aluno do
# ensino médio, deverá mostrar mensagem para ser digitado a
# nota do 1º, 2º, 3º e 4º bimestre. Após deverá mostrar na tela se o aluno foi aprovado, se está em recuperação ou foi reprovado
# sem chance de recuperação.
# Lembrando que cada bimestre vale 25 pontos num total anual de 100 pontos.

nota1 = float(input("qual nota o aluno alcançou no 1º Bimestre? "))
nota2 = float(input("qual nota o aluno alcançou no 2º Bimestre? "))
nota3 = float(input("qual nota o aluno alcançou no 3º Bimestre? "))
nota4 = float(input("qual nota o aluno alcançou no 4º Bimestre? "))
notafinal = (nota1 + nota2 + nota3 + nota4)

if(notafinal >= 60 <= 100):
        print("Aluno Aprovado, ")
elif(notafinal >= 40 <= 60 ):
        print("Aluno em Recuperação")
elif(notafinal < 40 >= 0):
        print("Aluno Reprovado(sem chance de recuperação)")