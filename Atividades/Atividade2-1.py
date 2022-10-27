# programa QUE receba 5 produtos em variáveis constantes e calcula o valor da compra com a quantidade de produtos
# comprados adicionando desconto e juros.

iph = 2980.00
sam = 2540.00
tab = 1950.00
ps5 = 2100.00
notb = 2350.00

qtd_iph = int(input("qual a contidade de Iphone deseja comprar? "))
qtd_sam = int(input("qual a contidade de Samsung deseja comprar? "))
qtd_tab = int(input("qual a contidade de tablet deseja comprar? "))
qtd_ps5 = int(input("qual a contidade de PlayStation 5 deseja comprar? "))
qtd_notb = int(input("qual a contidade de Notebook deseja comprar? "))

valort = (iph * qtd_iph) + (sam * qtd_sam) + (tab * qtd_tab) + (ps5 * qtd_ps5) + (notb * qtd_notb)
print("o valor total da compra é: ", valort)

valor6 = valort
valor10 = valort

valort = valort/3
print("o valor dividido em 3X sem juros é", valort)

valor6 = ((((valor6 * (5/100))+valor6)/6 ))
print("valor dividido em 6X com acréscimo de 5%", valor6)

valor10 = (valor10 - (valor10*(10/100)))
print("o valor total da compra a vista com 10% de desconto é", valor10)