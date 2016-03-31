from connexion import connexion

from services.installations.installations import Installations

def allInstallations():
	luste_installations = [] #On créer une liste vide

	db, curseur = conn.cursor()

	cursor.execute("SELECT InsNum, InsNom, adresse, code_postal, ville, longitude, latitude FROM installations") #On lance la requête pour récupérer les données de installations
	liste_installations = cursor.fetchall() #On met les données dans une variable

	for row in liste_installations: #On parcours notre variable 
		installations.append(Installations(row[1], row[0], row[7], row[4], row[2], row[9], row[10])) #On ajoute les données dans notre liste_installations
		
	db.commit()
	db.close()

	#installation = json.dumps(liste_installations) #On met la liste_activities en format JSON
	#print(installation)

	return installation #On retourne notre liste