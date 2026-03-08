# Exercício 8: Calcular a Média de 10 Notas e informar notas iguais ou acima da media 

al1 = float(input("Nota 1: "))
al2 = float(input("Nota 2: "))
al3 = float(input("Nota 3: "))
al4 = float(input("Nota 4: "))
al5 = float(input("Nota 5: "))
al6 = float(input("Nota 6: "))
al7 = float(input("Nota 7: "))
al8 = float(input("Nota 8: "))
al9 = float(input("Nota 9: "))
al10 = float(input("Nota 10: \n"))

media = (al1+al2+al3+al4+al5+al6+al7+al8+al9+al10) / 10

contador = 0

if al1 >= media:
    contador += 1
if al2 >= media:
    contador += 1
if al3 >= media:
    contador += 1
if al4 >= media:
    contador += 1
if al5 >= media:
    contador += 1
if al6 >= media:
    contador += 1
if al7 >= media:
    contador += 1
if al8 >= media:
    contador += 1
if al9 >= media:
    contador += 1
if al10 >= media:
    contador += 1

print("Média:", media)
print("Alunos com nota igual ou acima da média:", contador)