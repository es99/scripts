#!/home/engels/anaconda3/bin/python

"""
Script que compara dois arquivos .csv linha-a-linha, um arquivo tem o CPF e as entidades de acesso
e o outro só o nome o nome e CPF, então ele verificar se os CPF's são iguais e salva num novo arquivo
a entidade, cpf e nome da pessoa
"""

import os, csv

os.chdir('/home/engels/Infopublic/bancos/arquivos')

csvFile = open('csv_nomes.csv')
csv2File = open('csv2_entidade_cpf.csv')
csvReader_nomes = csv.reader(csvFile)
csv2Reader_cpf = csv.reader(csv2File)

nomes = []
cpf = []

for row in csvReader_nomes:
    nomes.append(row)

csvFile.close()

for row in csv2Reader_cpf:
    cpf.append(row)

csv2File.close()

linhas_oficiais = []
for i in range(len(nomes)):
    for j in range(len(cpf)):
        if nomes[i][5] == cpf[j][1]:
             nova_linha = cpf[j] + nomes[i]
             linhas_oficiais.append(nova_linha)
        else:
            continue

outputFile = open('lista_usuarios_entidades.csv', 'w', newline='')
outputWrite = csv.writer(outputFile)
contador = 0
for linha in linhas_oficiais:
    outputWrite.writerow(linha)
    contador += 1
outputFile.close()
print(contador + ' adicionadas no arquivo')
print('FIM')
