class Casa:

	def __init__(self, cor):
		self.cor = cor
		self.porta1 = False
		self.porta2 = False
		self.porta3 = False
		
	def pinta(self, cor):
		self.cor = cor
		
	def __str__(self):
		return self.cor
		
	def quantasPortasEstaoAbertas(self):
		count = 0
		if self.porta1 and self.porta2 and self.porta3 == False:
			count = 0
		elif self.porta1 and self.porta2 and self.porta3 == True:
			count += 3
		elif self.porta1 and self.porta2 == True:
				count += 2
		elif self.porta1 and self.porta3 == True:
				count += 2
		elif self.porta2 and self.porta3 == True:
				count += 2
		elif self.porta2 and self.porta1 == True:
				count += 2
		elif self.porta3 and self.porta2 == True:
				count += 2
		elif self.porta3 and self.porta1 == True:
				count += 2
		else:
			if self.porta1 or self.porta2 or self.porta3 == True:
				count += 1
		return count

		