# Exercício Loop: Identificar Números Pares e Ímpares

print("Digite uma sequancia de 10 numeros")
n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
n3 = int(input("Numero 3: "))
n4 = int(input("Numero 4: "))
n5 = int(input("Numero 5: "))
n6 = int(input("Numero 6: "))
n7 = int(input("Numero 7: "))
n8 = int(input("Numero 8: "))
n9 = int(input("Numero 9: "))
n10 = int(input("Numero 10: "))

pares = 0
inpar = 0

if n1%2 == 0:
    pares += 1 

else:
    inpar += 1

if n2%2 == 0:
    pares += 1 

else:
    inpar += 1

if n3%2 == 0:
    pares += 1 

else:
    inpar += 1

if n4%2 == 0:
    pares += 1 

else:
    inpar += 1  

if n5%2 == 0:
    pares += 1 

else:
    inpar += 1  

if n6%2 == 0:
    pares += 1 

else:
    inpar += 1

if n7%2 == 0:
    pares += 1 

else:
    inpar += 1  

if n8%2 == 0:
    pares += 1 

else:
    inpar += 1

if n9%2 == 0:
    pares += 1 

else:
    inpar += 1 

if n10%2 == 0:
    pares += 1 

else:
    inpar += 1   

print("Pares: ",pares,)   
print("Impares: ",inpar,)            


