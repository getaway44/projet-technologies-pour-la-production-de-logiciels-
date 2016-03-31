class Equipements:
	def __init__(self, EqId, InsNom, InsNum):
		self.EqId = EqId
		self.InsNom = InsNom
		self.InsNum = InsNum

	def __repr__(self):
		return "{} - {}".format(self.EqId, self.InsNom, self.InsNum)