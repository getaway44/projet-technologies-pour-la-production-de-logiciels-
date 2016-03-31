class InstallationLine:
	def __init__(self, numInstall, nomUsuelInstall, adresse, code_postal, ville, latitude, longitude):
		self.numInstall = numInstall
		self.nomUsuelInstall = nomUsuelInstall
		self.adresse = adresse
		self.code_postal = code_postal
		self.ville = ville
		self.latitude = latitude 
		self.longitude = longitude
	def __repr__(self):
		return "num: {} --  nom: {} -- adresse: {} -- codeP: {} -- ville: {} -- latitude: {} -- longitude: {} \n".format(self.numInstall, self.nomUsuelInstall, self.adresse, self.code_postal, self.ville, self.latitude, self.longitude)