import clases

print("========= PERSONA =========")
persona1 = clases.Persona()

persona1.setNombre("Carlos")
persona1.setApellido("Ruggeri")
persona1.setEdad(66)
print(persona1.getNombre())

print("========= INFORMÁTICO =========")
informatico1 = clases.Informatico()
informatico1.setNombre("Astor")
informatico1.setApellido("Piazolla")
informatico1.setEdad(66)
print(informatico1.getNombre())
print(informatico1.getLenguajes())
print(informatico1.getExperiencia())

print("========= DEVOPS =========")
devops1 = clases.Devops()
devops1.setNombre("Pedro")
devops1.setApellido("Devops")
devops1.setEdad(49)
print(devops1.getNombre())
print(devops1.getLenguajes())
print(devops1.getExperiencia())
print(devops1.deployar())