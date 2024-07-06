from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint (0,2)

print('''Suas opções
[0] Pedra
[1] Papel
[2] Tesoura''')
opcao = (int(input("Escolha um opção")))

print
print("---------------------------------------------")
print ("o computador escolheu {}".format(itens[computador]))
print ("Voce escolheu {}".format(itens[opcao]))
print("---------------------------------------------")
print

if computador == 0: #Pedra
     
    if opcao == 0:  #Pedra
        print("EMPATE") 
        
    elif opcao == 1: #papel
        print("JOGADOR VENCEU") 
        
    elif opcao == 2: #tesoura 
        print("COMPUTADOR VENCEU") 

elif computador == 1: #papel
    
    if opcao == 0:  #Pedra
        print("COMPUTADOR VENCEU") 
        
    elif opcao == 1: #papel
        print("EMPATE") 
        
    elif opcao == 2: #tesoura 
        print("JOGADOR VENCEU")
    
    
elif computador == 2: #tesoura 
    
    if opcao == 0:  #Pedra
        print("JOGADOR VENCEU") 
        
    elif opcao == 1: #papel
        print("COMPUTADOR VENCEU") 
        
    elif opcao == 2: #tesoura 
        print("EMPATE") 
    