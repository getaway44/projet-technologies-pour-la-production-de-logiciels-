from connexion import connexion
from importers.installations.InstallationLine import InstallationLine

def insertActivity(activity):
    conn = sqlite3.connect('installations.db')
    c = conn.cursor()
    insertQuery = "INSERT INTO activities(code, label) VALUES (?, ?)"
    c.execute(insertQuery, (activity.code, activity.label))
    conn.commit()
    conn.close()
