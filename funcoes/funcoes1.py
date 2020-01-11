numeros = []
pares = []
impares = []

for i in range(10):
    numeros.append(int(input('Entre com o número %s: ' % (i + 1))))

pares = filter(lambda valor : valor % 2 == 0, numeros)
impares = filter(lambda valor : valor %2 != 0, numeros)

print('Numeros pares: ')
for n in pares:
    print(n)

print('\nNúmeros ímpares: ')
for n in impares:
    print(n)
