"""
  Generar un password aleatorio de 8 caracteres de longitud, 
  que contenga al menos una letra mayúscula, 
  un número y un caracter especial.
"""

from Password import Password

password = Password()
password.setSecurePassword()
print(password.get())