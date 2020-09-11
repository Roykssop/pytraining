import mysql.connector 

# Inicio conexión
database = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="N3w_p@ssw0rD."
)

# Hubo conexión?
print(database)

# Cursor
cursor = database.cursor(buffered=True)

# Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS pytraining")
cursor.execute("SHOW DATABASES")

"""
for db in cursor:
  print(db)
"""

# Crear tabla
cursor.execute("USE pytraining")
cursor.execute("""CREATE TABLE IF NOT EXISTS vehiculos (
  id int(10) auto_increment not null,
  marca varchar(40) not null,
  modelo varchar(40) not null,
  precio float(10,2) not null,
  CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

"""
cursor.execute("SHOW TABLES")

for table in cursor:
  print(table)
"""

#  Insert registro
#cursor.execute("INSERT INTO vehiculos VALUES (null,'Ford','Fiesta',900000)")
vehiculos = [
  ('Renault','Kangoo',750000),
  ('Citroen','C4',750000)
]

#cursor.executemany("INSERT INTO vehiculos VALUES (null,%s,%s,%s)",vehiculos)
database.commit()

# Select Registros
cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()

print("======= LISTA DE VEHICULOS =======")
for vehiculo in result:
  print(vehiculo[1], vehiculo[3])

# Select primer registro
cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchone()

print("======= PRIMER VEHICULO =======")
print(result[1],result[3])