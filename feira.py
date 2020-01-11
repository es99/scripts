#!/home/engels/anaconda3/bin/python

"""
Programa que alimenta um dicionário com produtos e preços e exibe a lista dos
produtos e seus preços de forma bonita utilizando as funções rjust, ljust e center.
"""

feira = {}
def printFeira(dictFeira, largLeft, largRight):
    print('Itens da Feira'.center(largLeft + largRight, '='))
    for k, v in dictFeira.items():
        print(k.ljust(largLeft, '.') + str(v).rjust(largRight))

def adicionaItens(nItens):
    for i in range(nItens):
        xItem = input('Entre com o item que deseja adicionar: ')
        yItem = float(input('Entre com o preço do item: '))
        feira[xItem] = yItem

numeroItens = int(input('Quantos itens deseja adicionar? '))

adicionaItens(numeroItens)
printFeira(feira, 20, 5)
