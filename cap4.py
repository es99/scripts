#!/usr/bin/python3
# coding: utf-8

import sys

def novaLista(lista):
    lista[-1] = 'and ' + lista[-1]
    return ', '.join(lista)
    
del sys.argv[0]

print(novaLista(sys.argv))



