#!/usr/bin/python3
"""
Este programa gera um txt com uma série de perguntas de múltipla escolha sobre Engels
"""
import random

dados = {
    "Signo": ['Gêmeos', 'Câncer', 'Touro', 'Leão', 'Áries', 'Capricórnio'],
    "Gosta": ['Jogar Videogame', 'Dormir', 'Cerveja', 'Futebol', 'Guitarra'],
    "naoGosta": ['Acordar Cedo', 'Vodka', 'Fígado', 'Inverno', 'Golfe']
}

quizFile = open('teste_engels.txt', 'w')
quizFile.write("Nome:\n\nData:\n\n")
quizFile.write((' ' * 20) + "Teste para ver se você conhece Engels" + '\n\n')

quizFile.write('1. Qual o signo de Engels?\n')
signoCorreto = "Gêmeos"
respostaIncorreta = list(dados["Signo"])
del respostaIncorreta[respostaIncorreta.index(signoCorreto)]
respostaIncorreta = random.sample(respostaIncorreta, 4)
opcoes = respostaIncorreta + [signoCorreto]
random.shuffle(opcoes)

for i in range(5):
    quizFile.write('  %s. %s\n' % ('ABCDE'[i], opcoes[i]))
quizFile.write('\n\n')

quizFile.write('2. O que Engels gosta de fazer?\n')
oqGosta = list(dados["Gosta"])
oqGosta = random.sample(oqGosta, 1)
nGosta = list(dados["naoGosta"])
nGosta = random.sample(nGosta, 4)
opcoes2 = nGosta + oqGosta
random.shuffle(opcoes2)

for i in range(5):
    quizFile.write('  %s. %s\n' % ('ABCDE'[i], opcoes2[i]))
quizFile.write('\n\n')

quizFile.write('3. O que Engels não gosta de fazer?\n')
nGosta = random.sample(dados["naoGosta"], 1)
gosta = random.sample(dados["Gosta"], 4)
opcoes = gosta + nGosta
random.shuffle(opcoes)

for i in range(5):
    quizFile.write('  %s. %s\n' % ('ABCDE'[i], opcoes[i]))

quizFile.close()
