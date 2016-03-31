from importers.equipements.EquipementLine import EquipementLine

def parseRow(row):
    insNum = int(row[2].strip())
    insNom = str(row[3].strip())
    idE = row[4].strip()
    return EquipementLine(insNum, insNom, idE)