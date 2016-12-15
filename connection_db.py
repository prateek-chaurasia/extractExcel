import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'etl'
PASSWORD = 'root'
DBNAME = 'etl'

try:
	connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DBNAME)
except exception as e:
	print "Unable to connect to DB"

def readQuery(connection):
	cursor = connection.cursor()
	cursor.execute("SELECT * from EMPLOYEE")
	for row in cursor.fetchall():
		print row

readQuery(connection)
connection.close()

def createCursor(connection):
	"""This function returns a cursor and connection"""
	cursor = connection.cursor()
	return cursor, connection
	
