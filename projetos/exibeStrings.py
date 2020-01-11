#!/home/engels/anaconda3/bin/python

"""
Cria uma função chamada printTable() que recebe uma lista de listas de string
e exibe uma tabela bem organizada.
"""

tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

def printTable(listas):
    larguraCol = [0] * len(listas)
    for i in range(len(listas)):
        for j in range(4):
            palavra = listas[i][j]
            if len(palavra) > larguraCol[i]:
                larguraCol[i] = len(palavra)
    for i in range(4):
        for j in range(len(listas)):
            print(listas[j][i].rjust(max(larguraCol, key=int)), end='')
        print('\n')


printTable(tableData)
