#Questão 4: O Boletim Escolar Automático (Aritmética + Lógica AND)
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
percent_frequencia = int(input("Qual a frequência do aluno entre 0 e 100: "))

media = (n1 + n2) / 2

result = media >= 6.0 and percent_frequencia >= 75

print(result)