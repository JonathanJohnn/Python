
print("programa venda de produtos")
iphone = 2980
samsung = 2540
tablet = 1950
ps5 = 2100
notebook = 2350

print("o valor do Iphione é R$: ")
totaliphone = iphone * float(input("quantos deseja comprar? "))
print(totaliphone)

print("o valor do Samsung é R$: ")
totalsamsung = samsung * float(input("quantos deseja comprar? "))
print(totalsamsung)

print("o valor do Tablet é R$: ")
totaltablet = tablet * float(input("quantos deseja comprar? "))
print(totaltablet)

print("o valor do PS5 é R$: ")
totalps5 = ps5 * float(input("quantos deseja comprar? "))
print(totalps5)

print("o valor do Notebook é R$: ")
totalnotebook = notebook * float(input("quantos deseja comprar? "))
print(totalnotebook)

valortotal = totaliphone + totalsamsung + totaltablet + totalps5 + totalnotebook
print("o valor total da compra é R$: ", valortotal)

valortotal1 = valortotal/3
print("o valor total da compra em 3X sem juros é R$: ", valortotal1)


valortotal2 = ((((valortotal * (5/100))+valortotal)/6))
print("o valor total da compra em 6X com juros é R$: ", valortotal2)

valortotal3 = (valortotal - (valortotal*(10/100)))
print("o valor total da compra á vista com 10% de desconto é R$: ", valortotal3)