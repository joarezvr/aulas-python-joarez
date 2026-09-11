lista_funcionarios = []
lista_aumento = []
lista_demissao = []

print("ADICIONE OS FUNCIONARIOS DA SUA EMPRESA")
while True: # sisitema de adição
    while True: # adicionar alunos
        funcionario = input("Insira o nome do funcionario: ")
        lista_funcionarios.append(funcionario)

        opcao = input("Deseja continuar? [S/N]: ") #finalizar adição
        if opcao == "N":
            break

            for funcionario in lista_funcionarios:
                print(funcionario)





