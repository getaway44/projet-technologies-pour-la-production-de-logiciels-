from importers.installations.InstallationLine import InstallationLine

def parseRow(row):
    code = int(row[4].strip())
    label = row[5].strip()
    return ActivityLine(code, label)
