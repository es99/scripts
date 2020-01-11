#!/usr/bin/python3
"""
randomQuizGenerator.py - Cria provas com perguntas e respostas em ordem
aleatória, juntamente com gabaritos contendo as respostas.
"""

import random

capitais = {
    "Maranhão": "São Luís",
    "Paraíba": "João Pessoa",
    "Rio Grande do Norte": "Natal",
    "Pernambuco": "Recife",
    "São Paulo": "São Paulo",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Sul": "Porto Alegre",
    "Acre": "Rio Branco",
    "Tocantins": "Palmas",
    "Bahia": "Salvador",
    "Minas Gerais": "Belo Horizonte",
    "Distrito Federal": "Brasília",
    "Goiás": "Goiânia",
    "Ceará": "Fortaleza",
    "Piauí": "Teresina",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Pará": "Belém",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Alagoas": "Maceió",
    "Sergipe": "Aracaju",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Espírito Santo": "Vitória",
    "Paraná": "Curitiba",
    "Santa Catarina": "Florianopolis"
}

#Gera 35 arquivos contendo as provas
for numProva in range(35):
    #Cria os arquivos das provas e dos gabaritos de resposta
    provaFile = open("./provas/Prova-%s.txt" % (numProva + 1), "w")
    gabaritoFile = open("./provas/Gabarito-%s.txt" % (numProva + 1), "w")

    #Escreve o cabeçalho das provas
    provaFile.write("Nome:\n\nData:\n\nMatrícula:\n\n")
    provaFile.write((' ' * 20) + "Prova sobre Estados e suas respectivas capitais (Prova %s)" % (numProva + 1))
    provaFile.write('\n\n')

    #Embaralha a ordem dos Estados
    estados = list(capitais.keys())
    random.shuffle(estados)

#Percorre todos os estados em loop, criando uma pergunta para cada um
    for questionNum in range(27):

        respostaCorreta = capitais[estados[questionNum]]
        respostasErradas = list(capitais.values())
        del respostasErradas[respostasErradas.index(respostaCorreta)]
        respostasErradas = random.sample(respostasErradas, 3)
        opcoesRespostas = respostasErradas + [respostaCorreta]
        random.shuffle(opcoesRespostas)

        #Grava a pergunta e as opções de resposta no arquivo de prova.
        provaFile.write('%s. Qual a capital do estado: %s\n' % (questionNum + 1,  estados[questionNum]))
        for i in range(4):
            provaFile.write('   %s. %s\n' % ('ABCD'[i], opcoesRespostas[i]))
        provaFile.write('\n')

        #Grava o gabarito com as respostas em um arquivo.
        gabaritoFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[opcoesRespostas.index(respostaCorreta)]))
    provaFile.close()
    gabaritoFile.close()
