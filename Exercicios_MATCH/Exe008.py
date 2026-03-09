# 8. Operação matemática
# Recebe uma operação (em texto) e dois números.
# Operações válidas: "soma", "subtrai", "multiplica", "divide".
# Exemplo:
# Entrada →
# Operação: "divide"
# Número 1: 20
# Número 2: 4
# Saída → 5


op = input("Operação (soma, subtrai, multiplica, divide): ")
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))

match op:
    case "soma":
        resultado = num1 + num2
    case "subtrai":
        resultado = num1 - num2
    case "multiplica":
        resultado = num1 * num2
    case "divide":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: divisão por zero"
    case _:
        resultado = "Operação inválida"

print(resultado)