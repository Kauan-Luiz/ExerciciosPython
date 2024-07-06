import random 

numero_secreto = random.randint(1, 10)

print("Acabei de pensar em um numero, consegue advinhar?")
num = int(input("diga seu palpite"))
if num == numero_secreto:
    print ("nice! acertou")   
else:       
    acertou = False
    palpite = 0
    while not acertou:
        num = (int(input("Errado! Tente novaente")))
        palpite =+ 1        
        if num == numero_secreto: 
            print("voce acertou")
        acertou = True       
print("jogo finalizado")
