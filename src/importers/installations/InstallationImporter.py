import csv

from importers.installations.InstallationLine import InstallationLine
from importers.installations.InstallationLineParser import parseRow
from importers.installations.InstallationCreator import insertInstallation

def importActivities(filename):
	importedActivities = []

	with open(filename, 'rt') as csvfile:
		activitiesReader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in activitiesReader:
			try:
				activityLine = parseRow(row)
				if activityLine.code not in importedActivities:
					insertActivity(activityLine)
					importedActivities.append(activityLine.code)
					# print(activityLine)
			except ValueError:
				print("Problem with row {} : {}".format(activitiesReader.line_num, ','.join(row)))

	csvfile.close()
