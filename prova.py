#!/usr/bin/python3

def soma(x, y, z):
    return x + y + z

def media(soma):
    media = int(soma) / 3
    return media

valor1 = input('Entre com o primeiro valor: ')
valor2 = input('Entre com o segundo valor: ')
valor3 = input('Entre com o terceiro valor: ')

print('A média dos 3 valores é: '+ str(media(soma(valor1, valor2, valor3))))



