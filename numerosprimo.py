num = (int(input("digite um numero")))

for C in range (1, num+1):
    if num % C == 0:
        print('\033[34m')
    else:
        print('\033[32m')
    print (C, end='')
       