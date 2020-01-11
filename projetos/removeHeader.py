#!/home/engels/anaconda3/bin/python
"""
Script que percorre todos os arquivos em um diretório em busca de arquivos que terminem
em .csv ao achar este arquivo ele remove a primeira linha e reescreve o arquivo sem o
cabeçalho
"""

import sys, os, csv

path = sys.argv[1]
os.chdir(path)


for arquivo in os.listdir(path):
    if arquivo.endswith('.csv'):
        arquivoFile = open(arquivo)
        arquivoReader = csv.reader(arquivoFile)
        novoNome = arquivo[:-4] + '-modificado.csv'
        escritaFile = open(novoNome, 'w', newline='')
        escritaWriter = csv.writer(escritaFile)

        for row in arquivoReader:
            if arquivoReader.line_num == 1:
                continue
            else:
                escritaWriter.writerow(row)

        arquivoFile.close()
        escritaFile.close()

    else:
        continue

#FIM
