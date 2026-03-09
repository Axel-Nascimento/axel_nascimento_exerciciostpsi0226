# 10. Jogo: Pedra, Papel ou Tesoura
# Cria um programa que receba duas jogadas:
# •	Jogador 1
# •	Jogador 2
# Usa match para determinar o resultado:
# •	Pedra ganha de Tesoura
# •	Tesoura ganha de Papel
# •	Papel ganha de Pedra
# •	Se forem iguais, é Empate
# Exemplo:
# Entrada →
# Jogador 1: pedra
# Jogador 2: tesoura
# Saída → Jogador 1 venceu




jogador1 = input("Jogador 1: ")
jogador2 = input("Jogador 2: ")

match (jogador1, jogador2):
    
    case (j1, j2) if j1 == j2:
        resultado = "Empate"
    
    case ("pedra", "tesoura") | ("Pedra", "Tesoura") | ("PEDRA", "TESOURA") \
       | ("tesoura", "papel") | ("Tesoura", "Papel") | ("TESOURA", "PAPEL") \
       | ("papel", "pedra") | ("Papel", "Pedra") | ("PAPEL", "PEDRA"):
        resultado = "Jogador 1 venceu"
    
    case ("tesoura", "pedra") | ("Tesoura", "Pedra") | ("TESOURA", "PEDRA") \
       | ("papel", "tesoura") | ("Papel", "Tesoura") | ("PAPEL", "TESOURA") \
       | ("pedra", "papel") | ("Pedra", "Papel") | ("PEDRA", "PAPEL"):
        resultado = "Jogador 2 venceu"
    case _:
        resultado = "Jogada inválida"

print(resultado)