import mysql.connector 

# Inicio conexión
database = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="N3w_p@ssw0rD."
)

# Hubo conexión?
print(database)

cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS pytraining")
cursor.execute("SHOW DATABASES")

for db in cursor:
  print(db)


