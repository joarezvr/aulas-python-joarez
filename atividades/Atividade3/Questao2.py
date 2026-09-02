#Questão 2: A Fábrica de Caixas (Operador de Módulo)
total_macas = int(input("Qual o total de maçãs colhidas no dia? "))
total_caixas = int(total_macas / 12)
resto = total_macas % 12

print("O total de maçãs colhidas no dia foi: {}".format(total_macas))
print("O total de caixas com 12 maçãs em cada caixa foi: {}".format(total_caixas))
print("O total de maçãs que sobraram foi: {}".format(resto))
