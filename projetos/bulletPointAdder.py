#!/home/engels/anaconda3/bin/python

"""
Separa as linhas copiadas do clipboard e insere um * no início de todas elas
"""

import pyperclip

text = pyperclip.paste()

text = text.split('\n')

for i in range(len(text)):
    text[i] = '* ' + text[i]

text = '\n'.join(text)
print(text)
