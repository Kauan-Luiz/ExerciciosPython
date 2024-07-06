soma = 0 
cont = 0
contpar = 0
for C in range(1, 7):
    num = int(input("digite um valor"))
    cont = cont + 1
    if num % 2 == 0:
        contpar = contpar + 1
        soma = soma + num
print ("voce informou {} numeros, deste numeros {} foram par e o resultado foi de {}".format(cont, contpar, soma))  