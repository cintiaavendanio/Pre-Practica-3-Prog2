class Vehiculo():  # Definicion de la clase. 

    def __init__(self,nombre,ruedas,color): #Constructor.
        self.nombre=nombre
        self.ruedas=ruedas
        self.color=color
        self.enMarcha=False

    def arrancar(self):
        self.enMarcha = True


    def tipoVehiculo(self):
        if self.ruedas == 4:
            return "automovil"
        elif self.ruedas == 2:
            return "motocicleta"


    
    def mostrar(self):
        print("marca: {}  \nruedas: {} \ncolor: {}".format(self.nombre, self.ruedas, self.color))

#objetos
v1=Vehiculo("fiat1", 4, "rojo") 
v2=Vehiculo("zanelita", 2, "negro" )


print("Vehiculo 1:")
v1.mostrar()
print("tipo de vehiculo: ", v1.tipoVehiculo())

print("\nVehiculo 2:")
v2.mostrar()
print("tipo de vehiculo: ", v2.tipoVehiculo())

"""
Comisión: com 6/7
Grupo: 8
Integrantes:
-51709 Avendaño, Cintia Esther
-51658 Bernardi, Mateo
-51671 Rodriguez, Joaquin 
-51720 Novo, Luisina 
"""