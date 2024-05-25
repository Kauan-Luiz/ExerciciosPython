num1 = (int(input("informe o primeiro numero")))
num2 = (int(input("informe o segundo numero")))

if num1 > num2:
    print("o primeiro valor {}  é maior que o valor {}".format(num1, num2))
elif num2 > num1:
    print ("o segundo valor {} é maior que o valor {}".format (num2, num1))
elif num1 == num2:
    print ("os numeros sao iguais porra")