#!/home/engels/anaconda3/bin/python
import sys, pyperclip

"""
Este script salva senhas em um dicionário, e copia para a área de transferência
a senhas das contas que são passados como argumentos na linha de comando
"""

passwords = {
    'gmail': '@cesso#suporte..',
    'outlook': 'm@st3rcmsi.*',
    'infopublic': '#info8116*',
    'servidores': 'Infopublic#ts01_8116*',
    'linux': 'engelsink666',
    'cpfDiego': '06119361430'
}


if len(sys.argv) < 2:
    print('É necessário informar o nome da conta, ex (./gerenciador_senhas.py email)')
    sys.exit()

conta = sys.argv[1]

if conta in passwords:
    pyperclip.copy(passwords[conta])
    print('Senha da conta ' + conta + ' copiado para a área de transferência!')
else:
    print('A conta digitada não foi localizada no dicionário')
