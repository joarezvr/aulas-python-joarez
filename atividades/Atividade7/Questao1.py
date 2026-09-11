lista_funcionario = []
lista_demitidos = []
lista_aumento = []
opcao = "S"
cont = 0
while opcao == "S":
    print("Ficha de cadastro de funcionarios. Cadastre no minimo 4 funcionarios ")
    while True:
        if opcao == "S":
            nome = input("Digite o nome do Funcionario: ")
            lista_funcionario.append(nome)
            cont += 1
            if cont >= 4:
                opcao=input("Dseja cadastrar outro funcionario? Digite 'S' para continuar ou 'N' para finalizar ")
            elif opcao == "N":
            print("Abaixo está a lista de funcionarios cadastrados, demitidos e quem recebera o aumento")
            print("Lista de funcionários")
            for f in lista_funcionario:
                print(f)
            lista_demitidos.append((lista_funcionario[0],lista_funcionario[2]))
            print()
            print("Lista de funcionários demitidos")
            for d in lista_demitidos:
                print(d)
            print()
            lista_aumento.append(lista_funcionario[1])
            print("Lista de funcionários que receberão aumento")
            for a in lista_aumento:
                print(a)
            break
        else:
            opcao=input("Opção invalida. Digite 'S' para continuar ou 'N' para finalizar: ")