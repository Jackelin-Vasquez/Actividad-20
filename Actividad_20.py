class Empleado:
    def __init__(self,codigo,nombre,puesto,salario):
        self.__codigo= codigo
        #El codigo debe ser privado porque es un dato que identifica al empleado y si es modificado
        #puede causar que los datos del empleado tambien se vean afectados o que datos de otros empleados
        #sean sobre escritos, por ello para mayor seguridad no debe tener acceso a dicho dato.
        self.nombre=nombre
        #El nombre es un dato que se puede consultar en cualquier parte del codigo, no deberia existir
        #problemas al dejarlo publico.
        self._puesto=puesto
        self._salario= salario
        #el salario y puesto pueden cambiar, ya que el empleado puede tener un aumento o un acenso,
        #por ello son datos protegidos, pueden modificarse dentro de la clase por medio de metodos.

class Departamento:
    def __init__(self,codigo_interno,nombre):
        self.__codigo_interno=codigo_interno
        #El codigo es privado, ya que es un dato que no debe ser modificado fuera de la clase al ser
        #el identificador unico y su modificación puede causar problemas en toda la información que maneja.
        self.nombre= nombre
        #El nombre es un dato publico porque su consulta en distintas partes del codigo no deberia afectar
        #en su funcionamiento, e incluso puede llegar a cambiar el nombre del departamento por distintos motivos.
        self._empleados = []
        #la lista de empleados debe ser protegida porque su manipulación debe ser controlada, y esto
        #se puede realizar por medio de metodos de la clase.

class Empresa:
    def __init__(self,nombre,numero_registro):
        self.__nombre= nombre
        self.__numero_registro= numero_registro
        self._departamentos= []


def menu():
    print("---MENÚ---")
    print(f"1.Agregar empleados a un departamento.\n2.Mostrar información de un empleado.\n3.Lista de empleados por departamento")
    print(f"4.Salir")