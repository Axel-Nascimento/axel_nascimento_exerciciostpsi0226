# Exercício 7: Calcular a Média de Notas com Pesos

nota1 = float(input("Digite a nota da prova 1: "))
nota2 = float(input("Digite a nota da prova 2: "))
nota3 = float(input("Digite a nota da prova 3: "))

media = (nota1*2 + nota2*3 + nota3*5) / 10 

print("Média: ", media)

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado") 