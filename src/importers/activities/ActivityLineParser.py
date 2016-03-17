from importers.activities.ActivityLine import ActivityLine

def parseRow(row):
    equi = int(row[2].strip())
    actC = int(row[4].strip())
    actL = row[5].strip()
    return ActivityLine(equi, actC, actL)
