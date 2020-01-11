class Fila:

    def __init__(self):
        self.fila = []

    def entrar(self, nome):
        self.fila.append(nome)
        print('%s entrou na fila' % (nome))
    def sair(self):
        self.fila.pop(0)
