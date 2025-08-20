class Empleado:
    def __init__(self,codigo,nombre,puesto,salario):
        self.codigo= codigo
        self.nombre=nombre
        self.puesto=puesto
        self.salario= salario

class Departamento:
    def __init__(self,codigo_interno,nombre):
        self.codigo_interno=codigo_interno
        self.nombre= nombre
        self.empleados = []
class Empresa:
    def __init__(self,nombre,numero_registro):
        self.nombre= nombre
        self.numero_registro= numero_registro
        self.departamentos= []


def menu():
    print("---MENÚ---")