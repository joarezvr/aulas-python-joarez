#Questão 1: A Divisão da Conta (Calculadora)
valor_conta = float(input("Digite o valor do conta: "))
qtd_pessoas = float(input("Digite a quantidade de pessoas: "))
divisao = valor_conta / qtd_pessoas

print("O valor total da conta é: {}, e cada pessoa deve pagar R$ {}".format(valor_conta,divisao))

