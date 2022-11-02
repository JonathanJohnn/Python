# Numa fazenda em um local reservado para criação coloca-se um casal de coelhos. Supondo que em cada mês, a partir do
# segundo mês de vida, cada casal dá origem a um novo casal de coelhos, ao fim de um ano, quantos casais de coelhos
# estão no pátio? Escreva um programa para calcular a quantidade de coelhos em um ano.


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("quantos meses de criação? "))

if nterms <= 0:
   print("número invalido")
else:
   print("o total de casal por mês é:")
   for i in range(nterms):
       print(recur_fibo(i))
