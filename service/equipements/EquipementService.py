from connexion import connexion

from services.equipements.Equipements import Equipements

def allEquipements():
	liste_equipements = [] #On créer une liste vide

	db, curseur = conn.cursor()

	cursor.execute("SELECT EqId, InsNom, InsNum FROM equipements") #On lance la requête pour récupérer les données de equipements
	liste_equipements = cursor.fetchall() #On met les données dans une variable

	for row in liste_equipements: #On parcours notre variable
		equipements.append(Equipements(row[0], row[1], row[2])) #On ajoute les données dans notre liste_equipements
		# print(row)

	db.commit()
	db.close()

	#equipment = json.dumps(liste_equipement) #On met la liste_aquipements en format JSON
	#print(equipement)

	return lisye_equipements #On retourne notre liste