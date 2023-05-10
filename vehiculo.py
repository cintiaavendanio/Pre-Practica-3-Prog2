class Vehiculo():  # Definicion de la clase. Esto es el estado incial
    marca = str
    ruedas = int
    color = str
    enMarcha = bool

def __init__(self,nombre,ruedas,color):
    self.nombre=nombre
    self.ruedas=ruedas
    self.color=color



def arrancar(self):
    self.enMarcha = True


def tipoVehiculo(self):
    if self.ruedas == 4:
        return "automovil"
    elif self.ruedas == 2:
        return "motocicleta"



def mostrar(self):
    print("marca: {} , ruedas: {}, color: {}".format(self.marca, self.ruedas, self.color))


auto1=Vehiculo("fiat1", 4, "rojo")
auto1.mostrar()