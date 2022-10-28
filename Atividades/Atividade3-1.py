# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
# Mostre a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Informe o turno ao qual você estuda (M para Matutino, V para Vespertino e N para Noturno, as letras "
              "precisam estar em maiusculo) ")

match turno:
    case ("M"):
        print("Bom Dia!")
    case ("V"):
        print("Boa Tarde!")
    case ("N"):
        print("Boa Noite!")
    case _:
        print("valor Invalido")
