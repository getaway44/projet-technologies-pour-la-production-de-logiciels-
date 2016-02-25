import csv
def read(path):
	fichier = csv.reader(open(path, "rt"), delimiter=',')

	for row in fichier:
		print(row[0], row[1], row[2], row[4], row[7], row[9], row[10]) # Affiche les colonnes : "Nom usuel de l'installation", "Numéro de l'installation", "Nom de la commune", "Code postal", "Nom de la voie", "Longitude" et "Latitude".

if __name__ == '__main__':
    read("/hometu/etudiants/c/h/E145530K/Documents/Info2/Tech Prod Logiciel/projet-technologies-pour-la-production-de-logiciels-/csv/installations.csv")