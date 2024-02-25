#Lo que esta comentado es para la ejecucion del segundo metodo
class Persona:
    edad=27
    nombre="jose"
    #pais="chile"

doctor = Persona()
print(f"antes era{doctor.nombre}")
setattr(doctor,"nombre", "Hector")#para cambiar valor del atributo
print(f"ahora es: {doctor.nombre}")
#delattr(Persona, "pais") para eliminar
print(doctor.nombre)
print(doctor.edad)
#print(doctor.pais)