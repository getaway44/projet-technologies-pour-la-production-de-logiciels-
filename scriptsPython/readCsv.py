import csv
def read(nomFichier):
	if(nomFichier == "installations"):
		fichier = csv.reader(open("/hometu/etudiants/s/e/E145725X/semestre4/python/projet-technologies-pour-la-production-de-logiciels-/csv/installations.csv", "rt"), delimiter=',')
		for row in fichier:
			print(row[0], row[1], row[2], row[3], row[7], row[9], row[10])
	
	elif(nomFichier == "equipements"):
		fichier = csv.reader(open("/hometu/etudiants/s/e/E145725X/semestre4/python/projet-technologies-pour-la-production-de-logiciels-/csv/equipements.csv", "rt"), delimiter=',')
		for row in fichier:
			print(row[3], row[4])
		
	elif(nomFichier == "activites"):
		fichier = csv.reader(open("/hometu/etudiants/s/e/E145725X/semestre4/python/projet-technologies-pour-la-production-de-logiciels-/csv/activites.csv", "rt"), delimiter=',')
		for row in fichier:
			print(row[4], row[5])

if __name__ == '__main__':
	read(input())
