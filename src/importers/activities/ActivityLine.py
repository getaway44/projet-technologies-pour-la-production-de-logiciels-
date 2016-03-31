#class activité qui représente l'objet activité

class ActivityLine:

	#constructeur de la classe avec les deux attributs actcode et actlib
	def __init__(self, actCode, actLib):
		self._ActCode = actCode
		self._ActLib = actLib


	#méthode qui retourne l'actcode de l'activité
	def _get_ActCode(self):
		return self._ActCode

	#méthode qui set l'actcode de l'activité avec le parametre aC
	def _set_ActCode(self, aC):
		self._ActCode = aC

	#méthode qui retourne l'actLib de l'activité
	def _get_ActLib(self):
		return self._ActLib

	#méthode qui set l'actcode de l'activité avec le parametre aL
	def _set_ActLib(self, aL):
		self._ActLib = aL