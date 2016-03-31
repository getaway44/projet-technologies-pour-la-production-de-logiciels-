from connexion import connexion
from importers.activities.ActivityLine import ActivityLine


def insertActivity(activity):
	#on insctancie d'abord la connexion à la base de donnée
	conn = connexion()

	#on instancie le cursor en lui indiquant que les requêtes que nous allons lui envoyer seront de types "prepared"
	cursor = conn.cursor(prepared=True)

	#premiere partie de la requête
	insertQuery = "INSERT INTO activities(ActCode, ActLib) VALUES (?, ?)"

	#Les valeurs que l'ont insère
	cursor.execute(insertQuery,(activity._ActCode, activity._ActLib))


			#test: insertQuery = "INSERT INTO activities(ActCode, ActLib) VALUES (?, ?)"
			#cursor.execute(insertQuery,(111111,"Nicolas"))
			#attendu: un ligne actCode = 111111 et actLib = Nicolas
	
	#sauvegarde et fereture de la connexion
	conn.commit()
	conn.close()
