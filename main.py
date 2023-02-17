class Asiento:
        #Atributos
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    #metodos
    def cambiarColor(self,color):
        colores = ("rojo","verde","amarillo","negro","blanco")
        if color in colores:
            self.color = color

class Motor:
    #atributos
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    #metodos
    def cambiarRegistro(self,registro):
        self.registro = registro
    
    def asignatTipo(self,tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo

class Auto:
    #atributos
    cantidadCreados = 0
    def __init__(self, marca, modelo, precio, asientos, motor, registro):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.motor = motor
        self.registro = registro

    #metodos
    def cantidadAsientos(self):
        n_asientos = 0
        for asiento in self.asientos:
            if asiento != None:
                n_asientos += 1

    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for asiento in self.asientos:
                if asiento != None: return "Las piezas no son originales"
        return "Auto original"