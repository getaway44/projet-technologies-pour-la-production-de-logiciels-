from connexion import connexion
from importers.equipements.EquipementLine import EquipementLine

def insertEquipement(equipement):
	conn = connexion()
	cursor = conn.cursor(prepared=True)
	insertQuery = "INSERT INTO equipements(InsNumeroInstall, InsNom, EquipId) VALUES (?, ?, ?)"
	cursor.execute(insertQuery,(equipement.num, equipement.nom, equipement.id))
	conn.commit()
	conn.close()
