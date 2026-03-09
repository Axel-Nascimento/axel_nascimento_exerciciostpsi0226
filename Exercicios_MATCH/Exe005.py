# 5. Análise de mensagem
# Recebe uma mensagem e retorna:
# •	“Saudação” se for “olá” ou “bom dia”
# •	“Pergunta” se terminar com “?”
# •	“Despedida” se contiver “tchau” ou “adeus”
# •	“Mensagem genérica” caso contrário
# Exemplo:
# Entrada → “Tudo bem?”
# Saída → Pergunta



mensagem = input("Digite uma mensagem: ")

match mensagem:
    case "olá" | "ola" | "bom dia":
        resultado = "Saudação"
    case _:
        if "?" in mensagem:
            resultado = "Pergunta"
        elif "tchau" in mensagem or "adeus" in mensagem:
            resultado = "Despedida"
        else:
            resultado = "Mensagem genérica"

print(resultado)