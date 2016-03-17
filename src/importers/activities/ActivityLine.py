class ActivityLine:
	def __init__(self, equ, actCode, actLib):
		self._EquipementId = "equ"
		self._ActCode = "actCode"
		self._ActLib = "actLib"

	def _get_EquipementId(self):
		return self._EquipementId

	def _set_EquipementId(self, e):
		self._EquipementId = e

	def _get_ActCode(self):
		return self._ActCode

	def _set_ActCode(self, aC):
		self._ActCode = aC

	def _get_ActLib(self):
		return self._ActLib

	def _set_ActLib(self, aL):
		self._ActLib = aL
