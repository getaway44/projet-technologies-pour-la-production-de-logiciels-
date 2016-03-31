					#######################################################################################
					#fichier que l'on éxécute pour importer toutes les informations dans la base de donnée#
					#######################################################################################

from importers.activities.ActivityImporter import importActivities
from importers.installations.InstallationImporter import importInstallation
from importers.equipements.EquipementImporter import importEquipement
from admin.DatabaseAdmin import createTable


createTable()
importActivities('../data/activites.csv')
importEquipement('../data/equipements.csv')
importInstallation('../data/installations.csv')