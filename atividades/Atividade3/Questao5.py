#Questão 5: O Sistema de Desconto (Lógica OR)
valor_compra = float(input("Qual o valor da compra: "))
vip = int(input("Você é cliente VIP? (digite 1 para 'Sim, sou VIP' ou 0 para 'Não sou VIP'): "))

desconto = valor_compra > 200.00 or vip == 1

print(desconto)
