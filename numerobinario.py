
num = (int(input("informe um numero decima para transformar:")))
print("1 - base decimal para binario")
print("2 - base decima para octal")
print("3 - base decimal para hexadecima")

lista = (int (input("informe o nome do que deseja fazer")))

if lista == 1:
    print("o {} convertido para binario é de {}".format(num, bin(num)[2:]))
elif lista == 2:
    print ("o numero {} convertido para octal é de{}".format(num, oct(num)[2:]))
elif lista == 3:
    print ("o numero {} convertido para hexadecimal é de{}".format(num, hex(num)[2:]))

    