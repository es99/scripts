#!/home/engels/anaconda3/bin/python
"""
Script que percorre todos os arquivos em um diretório em busca de arquivos que terminem
em .csv ao achar este arquivo ele remove a primeira linha e reescreve o arquivo sem o
cabeçalho
"""

import sys, os, csv

path = sys.argv[1]
os.chdir(path)

os.makedirs('modificados', exist_ok=True)

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue

    print('removendo a primeira linha do arquivo ' + csvFilename + '...')
    csvRows = []
    arquivoFile = open(csvFilename)
    arquivoReader = csv.reader(arquivoFile)
    for row in arquivoReader:
        if arquivoReader.line_num == 1:
            continue
        csvRows.append(row)
    arquivoFile.close()

    escritaFile = open(os.path.join('modificados', csvFilename), 'w', newline='')
    escritaObj = csv.writer(escritaFile)
    for linha in csvRows:
        escritaObj.writerow(linha)
    escritaFile.close()
