#Questão 7: O Formulário de Doação de Sangue (Múltiplas Condições)
idade = int(input("Digite sua idade: "))
peso = float(input("Digite o seu peso (ex. 54.2): "))

doador = idade >= 16 and idade <= 69 and peso > 50.0

print("Você poder ser doador? {}".format(doador))