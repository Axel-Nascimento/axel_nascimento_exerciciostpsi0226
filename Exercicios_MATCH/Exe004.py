# 4. Tipo de dado
# Analisa um valor e retorna o seu tipo:
# •	Número inteiro
# •	Número decimal
# •	String numérica
# •	String textual
# •	Lista
# •	Tipo desconhecido
# Exemplo:
# Entrada → [10, 20, 30]
# Saída → Lista

valor = input("Digite um valor: ")

match valor:
    case _:
        if "[" in valor and "]" in valor:
            resultado = "Lista"
        elif "." in valor:
            resultado = "Número decimal"
        elif "0" in valor or "1" in valor or "2" in valor or "3" in valor or "4" in valor or "5" in valor or "6" in valor or "7" in valor or "8" in valor or "9" in valor:
            resultado = "String numérica"
        elif "a" in valor or "e" in valor or "i" in valor or "o" in valor or "u" in valor:
            resultado = "String textual"
        else:
            resultado = "Tipo desconhecido"

print(resultado)
