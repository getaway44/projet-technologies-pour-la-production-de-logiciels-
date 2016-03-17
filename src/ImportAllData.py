from importers.activities.ActivityImporter import importActivities
#from importers.installations.InstallationImporter import importInstallation
#from importers.equipements.EquipementImporter import importEquipement
from admin.DatabaseAdmin import createActivityTable

# TODO import other data : installations, equipements

createActivityTable()
importActivities('../data/activites.csv')
