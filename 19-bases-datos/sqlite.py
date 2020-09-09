import sqlite3

# Conexión
conexion = sqlite3.connect('pruebas.db')

# Crear cursor
cursor = conexion.cursor()

# Crear table
"""
cursor.execute("CREATE TABLE IF NOT EXISTS products("+
"id INTEGER PRIMARY KEY AUTOINCREMENT, "+
"titulo varchar(255), "+
"descripcion text, "+
"precio int(255) "+
")");

# Guardar cambios
conexion.commit()
"""

# Insertar datos
"""
cursor.execute("INSERT INTO products VALUES (null,'Primer producto','Descripción de producto', 1300)")
conexion.commit()
"""

# Borrar registros
cursor.execute("DELETE FROM products")
conexion.commit()

# Bulk insert
productos = [
  ("Portatil","Buen pc", 700),
  ("Celular","Buen celular", 700),
  ("Placa Madre","Buena placa", 700),
  ("Tablet","Buen tablet", 700)
]

cursor.executemany("INSERT INTO products VALUES (null,?,?,?)",productos)
conexion.commit()

# Fetch datos
cursor.execute("SELECT * FROM products")
productos = cursor.fetchall()

for product in productos: 
  print(product)

# Fetch first
cursor.execute("SELECT descripcion FROM products")
productos = cursor.fetchone()

print(productos)

# Cerrar conexión
conexion.close()