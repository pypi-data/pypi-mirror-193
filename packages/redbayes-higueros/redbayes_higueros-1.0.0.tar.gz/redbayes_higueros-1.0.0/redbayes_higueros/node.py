class Nodo:
    def __init__(self, nombre, padres, p):
        self.nombre = nombre
        self.estados = []
        self.padres = padres
        self.p = p