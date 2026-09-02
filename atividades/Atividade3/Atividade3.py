print("Calculo de desconto")
valor_compra = float(input("Digite o valor do compra: "))
porcentagem_desconto = float(input("Digite o porcentagem de desconto: "))

valor_economizado = porcentagem_desconto * valor_compra
valor_desconto = valor_compra - valor_economizado

print("O valor total da compra é: {} e o valor do desconto aplicado foi: {}.".format(valor_compra,valor_economizado))
print("O valor pago foi: {}".format(valor_desconto))
