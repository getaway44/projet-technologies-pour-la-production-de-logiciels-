from connexion import connexion
from importers.activities.ActivityLine import ActivityLine

def insertActivity(activity):
	conn = connexion()
	cursor = conn.cursor(prepared=True)
	insertQuery = "INSERT INTO activities(id, ActCode, ActLib) VALUES (?, ?, ?)"
	cursor.execute(insertQuery,(activity._EquipementId, activity._ActCode, activity._ActLib))
	conn.commit()
	conn.close()
