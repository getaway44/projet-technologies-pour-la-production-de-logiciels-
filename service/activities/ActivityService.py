from connexion import connexion
import json
from Activity import Activity

def allActivities():
	liste_activities = [] #On créer une liste vide

	db, cursor = connexion()

	cursor.execute("SELECT * FROM activities") #On lance la requête pour récupérer les données de activities
	res = cursor.fetchall() #On met les données dans une variable

	for row in res: #On parcours notre variable 
		liste_activities.append(Activity(row[0], row[1])) #On ajoute les données dans notre liste_activities
	print(liste_activities)
	db.commit()
	db.close()

	#activity = json.dumps(liste_activities) #On met la liste_activities en format JSON
	#print(activity)

	return liste_activities #On retourne notre liste

if __name__ == '__main__':
	allActivities()