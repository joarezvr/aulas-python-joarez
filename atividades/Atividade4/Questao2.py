velocidade_max = 80

vel = int(input("Qual a velociadade atual do veículo? "))

if vel <= velocidade_max:
    print("Velocidade dentro do limite permitido")
else:
    print("Você voi multado por excesso de velocidade")