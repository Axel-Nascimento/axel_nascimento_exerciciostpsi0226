# 1. Tipo de dia
# Cria um programa que receba o nome de um dia da semana e diga se é dia útil ou fim de semana.
# Exemplo:
# Entrada → domingo
# Saída → Fim de semana

dia = input("Digite um dia da semana: ")

match dia:
    case "segunda" | "terça" | "terca" | "quarta" | "quinta" | "sexta":
        print("Dia útil")
    case "sábado" | "sabado" | "domingo":
        print("Fim de semana")
    case _:
        print("Dia inválido")