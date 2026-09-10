numero_secreto = 14
tentativas = 0
palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Digite seu palpite para o número secreto: "))
    tentativas += 1

print(f"Parabéns! Você acertou o número secreto em {tentativas} tentativas!")