# 6. Estado do servidor
# Recebe um dicionário com as chaves "status" e "tempo_resposta".
# Retorna:
# •	“Servidor ativo” se o status for “ok”
# •	“Servidor lento” se o status for “ok” e o tempo de resposta for maior que 200 ms
# •	“Servidor indisponível” se o status for “erro”
# •	“Estado desconhecido” caso contrário
# Exemplo:
# Entrada → {"status": "ok", "tempo_resposta": 350}
# Saída → Servidor lento


servidor = {"status": "ok", "tempo_resposta": 350}

status = servidor["status"]
tempo = servidor["tempo_resposta"]

status = input("Digite uma mensagem: ")

match status:
    case "ok":
        if tempo > 200:
            resultado = "Servidor lento"
        else:
            resultado = "Servidor ativo"
    case "erro":
        resultado = "Servidor indisponível"
    case _:
        resultado = "Estado desconhecido"

print(resultado)