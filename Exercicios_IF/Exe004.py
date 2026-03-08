# Exercício 4: Verificar se o Cheque Pode Ser Descontado

s = 500.00
c = 0.00
desc = True

print("Saldo : ",s, "Euros")

c = float(input("Insira o valor do cheque a ser descontado "))

if c >= s:
 print(" Não possui Saldo sufiente para descontar", c, "Euros")

else:
 print("Cheque descontado, Saldo atual: ",s-c, "Euros")


