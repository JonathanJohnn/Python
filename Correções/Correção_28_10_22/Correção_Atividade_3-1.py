# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
# Mostre a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("programa para realizar saudação do dia!")
turno = input("Informe o turno ao qual você estuda (M para Manha, T para Tarde e N para Noite, as letras "
              "precisam estar em maiusculo) ").upper()

match turno:
    case "M":
        print("Bom Dia!")

    case "T":
        print("Boa Tarde!")

    case "N":
        print("Boa Noite!")

    case _:
        print("valor Invalido")
