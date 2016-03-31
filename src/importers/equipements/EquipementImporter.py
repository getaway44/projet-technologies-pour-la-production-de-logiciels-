import csv

from importers.equipements.EquipementLine import EquipementLine
from importers.equipements.EquipementLineParser import parseRow
from importers.equipements.EquipementCreator import insertEquipement

def importEquipement(filename):
	importedEquipement = []

	with open(filename, 'rt') as csvfile:
		equipementsReader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in equipementsReader:
			try:
				#print(row)
				equipementLine = parseRow(row)
				if equipementLine.num not in importedEquipement:
					insertEquipement(equipementLine)
					importedEquipement.append(equipementLine.num)
			except ValueError:
				print("Problem with row {} : {}".format(equipementsReader.line_num, ','.join(row)))

	csvfile.close()