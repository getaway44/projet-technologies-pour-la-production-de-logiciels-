import mysql.connector as connector
try :
db = MySQLdb.connect(host = "infoweb", user = "E145725X", password = "E145725X",database = "E145725X")
except Exception as e:
	sys.exit('We cant get into the database')
cursor = db.cursor()
cursor.execute('SELECT * FROM text')
