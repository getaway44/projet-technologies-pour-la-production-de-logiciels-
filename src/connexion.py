import mysql.connector as connector

#méthode qui permet la connexion à la base de donnée 
def connexion():
	try:
		return connector.connect(host = "infoweb", user = "E145725X", password ="E145725X", database = "E145725X")
	except ValueError:
		print("connexion impossible")