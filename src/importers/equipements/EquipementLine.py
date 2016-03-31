class EquipementLine:
	def __init__(self, InsNum, InsNom, EquipId):
		self.num = InsNum
		self.nom = InsNom
		self.id = EquipId

	def _getnum(self):
		return self.num

	def _setnum(self, e):
		self.num = e

	def _getnom(self):
		return self.nom

	def _setnom(self, aC):
		self.nom = aC

	def _getid(self):
		return self.id

	def _setid(self, aL):
		self.id = aL