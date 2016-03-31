from importers.activities.ActivityLine import ActivityLine

#methode qui retourne un objet activityLine 
def parseRow(row):
	#en prenant comme actCode le 5ème élément de la ligne 
    actC = int(row[4].strip())

    #et en prenant comme actLib le 6ème élément de la ligne 
    actL = row[5].strip()

    #on retourne l'objet ActivityLine tout en le construisant
    return ActivityLine(actC, actL)
