#!/home/engels/anaconda3/bin/python
#   coding: utf-8

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def exibeGrid(listas):
    for i in range(6):
        for j in range(len(listas)):
            print(listas[j][i], end='')
        print('\n')

exibeGrid(grid)
