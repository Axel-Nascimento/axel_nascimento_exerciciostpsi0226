# 7. Classificação de produto
# Recebe um dicionário com as chaves "categoria" e "preco".
# Retorna:
# •	“Produto de luxo” se categoria for “eletrônico” e preço acima de 1000
# •	“Produto comum” se categoria for “eletrônico” e preço até 1000
# •	“Produto alimentar” se categoria for “alimento”
# •	“Categoria desconhecida” caso contrário
# Exemplo:
# Entrada → {"categoria": "eletrônico", "preco": 1500}
# Saída → Produto de luxo

produto = {"categoria": "eletrônico", "preco": 1500}

categoria = produto["categoria"]
preco = produto["preco"]



match categoria:
    case "eletrônico":
        if preco > 1000:
            resultado = "Produto de luxo"
        else:
            resultado = "Produto comum"
    case "alimento":
        resultado = "Produto alimentar"
    case _:
        resultado = "Categoria desconhecida"

print(resultado)