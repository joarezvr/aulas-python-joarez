lista_alunos = []
num_aluno = 0

print("ADICIONANDO ALUNOS NA LISTA DE CHAMADA")

while True:
    aluno = str(input("Digite o nome do aluno: "))
    lista_alunos.append(aluno)

    opcao = input("Quer continuar? [S/N] ")#finaliza a edição
    if opcao == "N":
        break

print("A SUA TURMA FICOU COM TODOS ESTES ALUNOS")
for aluno in lista_alunos:
    print(f"Nome do aluno: {num_aluno}: {aluno}")#imprime a lista de alunos
    num_aluno += 1