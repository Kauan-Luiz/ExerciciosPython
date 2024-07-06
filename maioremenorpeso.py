maior = 0
menor = 0 

for c in range(1, 6):
    peso = (float(input("informe o peso da pessoa")))
    
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor: 
            menor = peso 
        
print ("o maior peso foi de {}ok".format(maior)) 
print ("o menor peso foi de {}ok".format(menor))        
    
    