#Questão 6: O Erro de Verificação (Análise e Correção de Código)
senha_cadastrada = 1234
senha_digitada = input("Digite sua senha: ")
acesso_liberado = senha_cadastrada == senha_digitada
print("Acesso liberado?", acesso_liberado)

"""
Resposta
A falha acontece pq quando a variavel 'senha_digitada' recebe o dado
sem que seja declarada o tipo de dado que sera salvo, o imput por padrão
salva o dado do tipo imput, e neste caso o codigo está tentando comparar
o conteudo da variavel 'senha_cadastrada' que é do tipo INT, com o conteudo
da variavel 'senha_digitada' que é do tipo STR.

Solução
Para solucionar a falha, deve ser determinado o tipo de dado a ser salvo pelo 
input como INT, conforme o codigo abaixo

senha_cadastrada = 1234
senha_digitada = int(input("Digite sua senha: "))
acesso_liberado = senha_cadastrada == senha_digitada
print("Acesso liberado?", acesso_liberado)


"""