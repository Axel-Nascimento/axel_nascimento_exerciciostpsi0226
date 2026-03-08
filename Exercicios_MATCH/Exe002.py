# 2. Classificação de nota
# Lê uma nota (0–100) e retorna uma classificação:
# •	90 ou mais → Excelente
# •	70–89 → Bom
# •	50–69 → Suficiente
# •	Abaixo de 50 → Insuficiente

nota = int(input("Digite a nota (0 a 100): "))

match nota:
    case n if n >= 90:
        print("Excelente")
    case n if 70 <= n <= 89:
        print("Bom")
    case n if 50 <= n <= 69:
        print("Suficiente")
    case n if n < 50:
        print("Insuficiente")
    case _:
        print("Nota inválida") 
