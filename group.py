class Person:
    pass

idmr1997= Person()
idjs1991 = Person()

#objeto.atributo = valor 
idmr1997.nombre = input("Ingresa tu nombre: ")
idmr1997.edad = input("Ingresa tu edad: ")
idmr1997.pais = input("Ingresa tu pais de origen: ")

print(f"{idmr1997.nombre} tiene {idmr1997.edad} años")
print(f"nacio en: {idmr1997.pais}")