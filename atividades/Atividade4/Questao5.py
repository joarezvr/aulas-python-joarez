idade = int(input("Qual a sua idade? "))
vip = int(input("Você possui convite VIP? (digite '1' para SIM e '0' para NÃO) "))
oganiszador = int(input("Você é organizador do evento? (digite '1' para SIM e '0' para NÃO) "))

if idade >= 18 and vip == 1 or oganiszador == 1:
    print("Entrada PERMITIDA!")
else:
    print("Entrada NEGADA!")