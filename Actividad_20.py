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
    print(f"1.Agregar empleados a un departamento.\n2.Mostrar información de un empleado.\n3.Lista de empleados por departamento")
    print(f"4.Salir")