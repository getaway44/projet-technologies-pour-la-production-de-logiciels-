class Installations:
	def __init__(self, InsNum, InsNom, adresse, code_postal, ville, longitude, latitude):
		self.InsNum = InsNum
		self.InsNom = InsNom
		self.adresse = adresse
		self.code_postal = code_postal
		self.ville = ville
		self.longitude = longitude
		self.latitude = latitude

	def __repr__(self):
		return "{} - {}".format(self.InsNum, self.InsNom, self.adresse, self.code_postal, self.ville, self.longitude, self.latitude)