import csv
def read(path):
	fichier = csv.reader(open(path, "rt"))

	if(path == "/hometu/etudiants/c/h/E145530K/Documents/Info2/Tech Prod Logiciel/projet-technologies-pour-la-production-de-logiciels-/csv/installations.csv"):
		for row in fichier:
			print(row[0], row[1], row[2], row[3], row[7], row[9], row[10])

	elif(path == "/hometu/etudiants/c/h/E145530K/Documents/Info2/Tech Prod Logiciel/projet-technologies-pour-la-production-de-logiciels-/csv/equipements.csv"):
		for row in fichier:
			print(row[3], row[4])

	elif(path == "/hometu/etudiants/c/h/E145530K/Documents/Info2/Tech Prod Logiciel/projet-technologies-pour-la-production-de-logiciels-/csv/activites.csv"):
		for row in fichier:
			print(row[4], row[5])