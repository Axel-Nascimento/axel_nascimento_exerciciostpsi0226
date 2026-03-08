# Exercício 6: Desconto de Compra

desconto = 0

nome = (input("Olá digite seu nome: "))
compra = float(input("Digite o valor da sua compra: "))

if compra <= 200:
    desconto = compra*0.1
    print("Nome: ",nome,)
    print("Compra: ",compra," Euros")
    print("Desconto: ",desconto, " Euros")
    print("Total a pagar: ",compra-desconto, " Euros")

elif compra >= 200.01 and  compra <= 500:
    desconto = compra*0.15
    print("Nome: ",nome,)
    print("Compra: ",compra," Euros")
    print("Desconto: ",desconto, " Euros")
    print("Total a pagar: ",compra-desconto, " Euros")

elif compra > 500:
    desconto = compra*0.20
    print("Nome: ",nome,)
    print("Compra: ",compra," Euros")
    print("Desconto: ",desconto, " Euros")
    print("Total a pagar: ",compra-desconto, " Euros")