# Exe 1 - Converter Segundos em Horas, Minutos e Segundos

stotal = int(input("Digite a quantidade de segundos: "))

srestante = stotal
hr = 0
min = 0

if srestante >= 3600:
    hr = srestante // 3600
    srestante = srestante - (hr * 3600)

if srestante >= 60:
    min = srestante // 60
    srestante = srestante - (min * 60)

seg = srestante

print(hr, "hora(s),", min, "minuto(s) e", seg, "segundo(s)")


 




