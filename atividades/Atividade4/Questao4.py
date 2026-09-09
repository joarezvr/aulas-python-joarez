saldo = 500

print(f"O seu saldo atual é {saldo}")

saque = float(input("Digite o valor do saque:"))

if saque <= saldo:
    saldo = saldo - saque
    print(f"Você sacou o valor de {saque}, e o seu saldo atual é de {saldo}")
else:
    print("Você não possui limite disponível para o valor que deseja sacar")


