#resposta

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
plano = bool(input("Você tem plano de saude: "))

dentro = (idade > 17 or idade < 55)

print("Ola {}, você tem {} anos, tem plano de saúde? {}. Você foi aceito? {}".format(nome,idade,plano,dentro))

print(plano)
print(dentro)