import csv

from importers.activities.ActivityLine import ActivityLine
from importers.activities.ActivityLineParser import parseRow
from importers.activities.ActivityCreator import insertActivity

#filename, le fichier que l'on va parcourir
def importActivities(filename):
	#tableau qui vas nous permettre de gérer les doublons
	importedActivities = []

	#on parcourt le fichier ligne par ligne
	with open(filename, 'rt') as csvfile:

		#retourne un un object "reader" qui va nous permettre de le lire ligne par ligne
		activitiesReader = csv.reader(csvfile, delimiter=',', quotechar='"')

		#on parcourt le fichier
		for row in activitiesReader:

			#si on reussi a effectuer ce qu'il y a dans le try, rien ne s afficher dans le terminal
					try:
						#pour debogage: print(row)

						#on récupère la ligne courante
						activityLine = parseRow(row)

						#gestion des doublons: si l'identifiant unique actCode n'est pas dans le tableau importedActivities, 
						#on l'ajoute et on et on l'insère dans la base de donnée sinon, on passe à la suivante 
						if activityLine._ActCode not in importedActivities:
							insertActivity(activityLine)
							importedActivities.append(activityLine._ActCode)
			#sinon, une exception est levée et dans le terminal est affichée les lignes qui posent problèmes
					except ValueError:
						print("Problem with row {} : {}".format(activitiesReader.line_num, ','.join(row)))
	#on ferme le csv reader
	csvfile.close()
