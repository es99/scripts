#!/usr/bin/python3
#   coding: utf-8

while(True):
    print('Entre com sua idade: ')
    idade = input()
    if idade.isdecimal():
        break
    print('Por favor, digite um numero pra sua idade!')

while(True):
    print('Entre com sua senha: ')
    senha = input()
    if senha.isalnum():
        break
    print('Senhas só podem contar letras e números!')
