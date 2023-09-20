import math

class ConversorDeAngulos:
    def __init__(self, angulo):
        self.angulo = angulo

    def grados_a_radianes(self):
        radianes = self.angulo * (math.pi / 180)
        return radianes

    def radianes_a_grados(self):
        grados = self.angulo * (180 / math.pi)
        return grados