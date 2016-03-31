import csv

from importers.installations.InstallationLine import InstallationLine
from importers.installations.InstallationLineParser import parseRow
from importers.installations.InstallationCreator import insertInstallation

def importInstallation(filename):
	importedInstallations= []

	with open(filename, 'rt') as csvfile:
		installationsReader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in installationsReader:
			try:
				InstallationLine = parseRow(row)
				if InstallationLine.numInstall not in importedInstallations:
					insertInstallation(InstallationLine)
					importedInstallations.append(InstallationLine.numInstall)
			except ValueError:
				print("Problem with row {} : {}".format(installationsReader.line_num, ','.join(row)))

	csvfile.close()
