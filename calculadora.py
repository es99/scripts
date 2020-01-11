class Calculadora:
	
	def __init__(self, num1, num2):
		self.a = num1
		self.b = num2
		
	def soma(self):
		return self.a + self.b
	
	def subtracao(self):
		if self.a > self.b:
			return self.a - self.b
		else:
			print('{} é menor do que {}'.format(self.a, self.b))
			
	def multiplicacao(self):
		return self.a * self.b
	
	def divisao(self):
		try:
			return self.a / self.b
		except:
			print('Divisao por 0 não é válida!')
	