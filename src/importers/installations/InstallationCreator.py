from connexion import connexion
from importers.installations.InstallationLine import InstallationLine

def insertInstallation(installation):
	conn = connexion()
	cursor = conn.cursor(prepared=True)
	
	insertQuery = "INSERT INTO installations(numInstall, nomUsuelInstall, adresse, code_postal, ville, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?)"
	cursor.execute(insertQuery, (installation.numInstall, installation.nomUsuelInstall, installation.adresse, installation.code_postal, installation.ville, installation.latitude, installation.longitude))
	conn.commit()
	conn.close()