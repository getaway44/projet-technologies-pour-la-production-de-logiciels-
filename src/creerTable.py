import mysql.connector as connector

try :
    db = connector.connect(host = "infoweb", user = "E145725X", password ="E145725X",database = "E145725X")
except Exception as e:
    sys.exit('We cant get into the database')

cursor = db.cursor()

creer_table_acti = "CREATE TABLE IF NOT EXISTS activities (id INT PRIMARY KEY NOT NULL, ActCode INT, ActLib TEXT);"

creer_table_equip = "CREATE TABLE IF NOT EXISTS equipements(InsNumeroInstall INT PRIMARY KEY NOT NULL, InsNom TEXT, EquipId INT);"

creer_table_install = "CREATE TABLE IF NOT EXISTS installations(numInstall INT PRIMARY KEY NOT NULL, nomUsuelInstall TEXT, nomCommun TEXT, codePost INT, nomVoie TEXT, longitude FLOAT, latitude FLOAT);"

cursor.execute(creer_table_acti)

cursor.execute(creer_table_equip)

cursor.execute(creer_table_install)

db.close()