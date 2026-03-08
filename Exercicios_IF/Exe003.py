# Exercício 3: Mostrar Números em Ordem Crescente e Decrescente

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 < num2:
    print("Crescente:", num1, ",", num2)
    print("Decrescente:", num2, ",", num1)
else:
    print("Crescente:", num2, ",", num1)
    print("Decrescente:", num1, ",", num2)