import csv
def read(path):
	fichier = csv.reader(open(path, "rt"), delimiter=',')

	for row in fichier:
			print(row[2], row[4], row[5]) #Affiche les colonnes : "EquipementId", "ActCode" et "ActLib"

if __name__ == '__main__':
    read("/hometu/etudiants/c/h/E145530K/Documents/Info2/Tech Prod Logiciel/projet-technologies-pour-la-production-de-logiciels-/csv/activites.csv")
    