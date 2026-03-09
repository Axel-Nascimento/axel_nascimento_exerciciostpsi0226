# 9. Processamento de requisição
# Recebe um dicionário com as chaves "metodo" e "conteudo".
# Retorna:
# •	“Requisição GET recebida” se o método for “GET”
# •	“Requisição POST com dados válidos” se o método for “POST” e o conteúdo não estiver vazio
# •	“Requisição POST sem dados” se o método for “POST” e o conteúdo estiver vazio
# •	“Método não suportado” caso contrário
# Exemplo:
# Entrada → {"metodo": "POST", "conteudo": ""}
# Saída → Requisição POST sem dados


requisição = {"metodo": "POST", "conteudo": ""}

metodo = requisição["metodo"]
conteudo = requisição["conteudo"]

match metodo:
    case "GET":
        resultado = "Requisição GET recebida"
    case "POST":
        if conteudo != "":
            resultado = "Requisição POST com dados válidos"
        else:
            resultado = "Requisição POST sem dados"
    case _:
        resultado = "Método não suportado"

print(resultado)