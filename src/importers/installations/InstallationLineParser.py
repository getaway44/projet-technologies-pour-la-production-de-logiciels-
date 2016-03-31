from importers.installations.InstallationLine import InstallationLine

def parseRow(row):
  numInstall = int(row[1].strip())
  nomUsuelInstall = str(row[0].strip())
  adresse = str(row[7].strip())
  code_postal = int(row[4].strip())
  ville = str(row[2].strip())
  latitude = float(row[10].strip())
  longitude = float(row[9].strip())
  return InstallationLine(numInstall, nomUsuelInstall, adresse, code_postal, ville, latitude, longitude)
