from connexion import connexion

def createActivityTable():
	conn = connexion()
	cursor = conn.cursor()
    

	cursor.execute("DROP TABLE IF EXISTS activities")
	cursor.execute("DROP TABLE IF EXISTS installations")
	cursor.execute("DROP TABLE IF EXISTS equipements")
    

	creer_table_acti = "CREATE TABLE IF NOT EXISTS activities (id INT PRIMARY KEY NOT NULL, ActCode INT, ActLib TEXT);"
	creer_table_equip = "CREATE TABLE IF NOT EXISTS equipements(InsNumeroInstall INT PRIMARY KEY NOT NULL, InsNom TEXT, EquipId INT);"
	creer_table_install = "CREATE TABLE IF NOT EXISTS installations(numInstall INT PRIMARY KEY NOT NULL, nomUsuelInstall TEXT, nomCommun TEXT, codePost INT, nomVoie TEXT, longitude FLOAT, latitude FLOAT);"
	

	cursor.execute(creer_table_acti)
	cursor.execute(creer_table_equip)
	cursor.execute(creer_table_install)


	conn.commit()
	conn.close()
