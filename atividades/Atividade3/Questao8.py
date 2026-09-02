#Questão 8: A Calculadora de Lucro da Empresa
nome_produto = input("Digite seu nome do produto: ")
custo_fabrica = float(input("Digite seu custo de fabrica do produto: "))
preco_venda = float(input("Qual o valor de venda do produto: "))

lucro = preco_venda - custo_fabrica
valor_lucro = lucro > 20.0

print("O produto '{}' rendeu um lucro de R${}".format(nome_produto,lucro))
print("O lucro do produto foi bom? {}".format(valor_lucro))