valor = (float(input("qual o valor da casa que deseja comprar?")))
salario = (float(input("qual o salario do SR(SRA)?")))
anos = (float(input("em quantos anos voce deseja pagar?")))

prestacao = (valor/(anos * 12))
porcent_salario = (salario * 0.30)
if prestacao > porcent_salario:
    print("FINANCIAMENTO NEGADO")
else:
    print ("FINANCIAMENTO AUTORIZADO")