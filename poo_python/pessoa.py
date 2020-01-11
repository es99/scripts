class Pessoa:
    estado = "indefinido"

    def andar(self):
        print("a pessoa está andando...")
        self.estado = "andando"
    def correr(self):
        print("a pessoa está correndo...")
        self.estado = "correndo"
