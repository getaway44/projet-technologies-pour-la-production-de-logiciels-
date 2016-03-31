class Activity:
	def __init__(self, ActCode, ActLib):
		self.ActCode = ActCode
		self.ActLib = ActLib

	def __repr__(self):
		return "{} - {}".format(self.ActCode, self.ActLib)



