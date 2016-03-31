from connexion import connexion

def createTable():
	#on commence par initialiser la connexion et le curseur
	conn = connexion()
	cursor = conn.cursor()

	#on drop les tables si elles existent déjà
	cursor.execute("DROP TABLE IF EXISTS activities")
	cursor.execute("DROP TABLE IF EXISTS installations")
	cursor.execute("DROP TABLE IF EXISTS equipements")

	#string creer_table_acti qui contient la requête sql de la table activities si elle n'existe pas avec ActCode qui correspond au code de l'activite et ActLib qui correspond au libélé de l'activité
	creer_table_acti = "CREATE TABLE IF NOT EXISTS activities (ActCode INT PRIMARY KEY NOT NULL, ActLib TEXT);"

	#string creer_table_equip qui contient la requête sql de la table equipements si elle n'existe pas avec InsNumeroInstall qui est le numero de l'installation, InsNom qui est le nom de l'installation et EquiId qui est le numéro unique de l'equipement
	creer_table_equip = "CREATE TABLE IF NOT EXISTS equipements(InsNumeroInstall INT PRIMARY KEY NOT NULL, InsNom TEXT, EquipId INT);"

	#string creer_table_install qui contient la requête sql de la table installations si elle n'existe pas avec des numInstall qui correspond au numéro d'installation, nomUsuelInstall qui correspond au nom usuel de l'installation,  adresse, code_postal, ville, latitude, longitude
	creer_table_install = "CREATE TABLE IF NOT EXISTS installations(numInstall INT PRIMARY KEY NOT NULL, nomUsuelInstall TEXT, adresse TEXT, code_postal INT, ville TEXT, latitude FLOAT, longitude FLOAT);"

	#on envoie les requetes à la base de donnée
	cursor.execute(creer_table_acti)

	cursor.execute(creer_table_equip)

	cursor.execute(creer_table_install)

	#on sauvegarde les changements et on ferme la connexion
	conn.commit()
	conn.close()


