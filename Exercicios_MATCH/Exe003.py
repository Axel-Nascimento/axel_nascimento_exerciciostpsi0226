# #3. Tipo de pedido
# Recebe um dicionário com as chaves "tipo" e "valor".
# Exibe:
# •	“Compra de X€” se tipo for “compra”
# •	“Venda de X€” se tipo for “venda”
# •	“Pedido desconhecido” caso contrário
# Exemplo:
# Entrada → {"tipo": "venda", "valor": 250}
# Saída → Venda de 250€

tipo = input("É uma venda ou uma compra? ")
valor = int(input(f"Qual o valor da {tipo}? "))

match tipo:
    case "compra":
        print("Compra de:" ,valor,"€")
    case "venda":
        print("Venda de:" ,valor,"€")
    case _:
        print("Pedido desconhecido")


valor = int(input("Qual o valor da " + tipo + "? "))