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

    def mostrar_informacion(self):
        print("---DATOS DEL EMPLEADO---")
        print(f"Nombre:{self.nombre}\nCodigo:{self.__codigo}\nPuesto:{self._puesto}\nSalario:{self._salario}")

    def modificar_puesto(self,nuevo_puesto):
        self._puesto = nuevo_puesto

    def consultar_salario(self,nombre):
        if self.nombre == nombre:
            print(f"Nombre:{self.nombre} tiene un salario de {self._salario} ")
        else:
            print(f"{nombre} no ha sido encontrado")

    def modificar_salario(self,nuevo_salario):
        if nuevo_salario <= 0:
            print("El salario debe ser mayor a 0...")
        else:
            self._salario = nuevo_salario

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

    def ingresar_empleados(self):
        print("---Ingreso de Empleados---")
        codigo= input("Ingrese codigo de empleado:")
        nuevo_empleado = input("Ingrese nombre de Empleado:")
        puesto= input("Ingrese puesto de empleado:")
        salario= input("Ingrese salario de empleado:")
        Empleados= Empleado(codigo,nuevo_empleado,puesto,salario)
        self._empleados.append(Empleados)

    def lista_empleados(self):
        if not self._empleados:
            print("Lista vacia...")
        else:
            for indice,i in enumerate(self._empleados):
                print(f"{indice}. {i.mostrar_informacion()}")


class Empresa:
    def __init__(self,nombre,numero_registro):
        self.__nombre= nombre
        #El nombre de la empresa es privado porque el nombre de la empresa en ningun momento debe ser
        #modificado o debe manipularse.
        self.__numero_registro= numero_registro
        #El numero de registro es privado debido a que es el numero que hace unica a la empresa
        #y demuestra que esta registrada de forma legal y si se da la oportunidad de manipularse puede
        #ocasionar problemas en sus datos o incluso en aspectos legales.
        self._departamentos= []
        #La lista de departamentos es protegida, ya que no debe ser manipulable fuera de la clase o de
        #sus sub-clases, se puede manipular pero de una forma controlada.

    def mostrar_información(self):
        print(f"Numero Registro:{self.__numero_registro}\nNombre:{self.__nombre}")

    def agregar_departamento(self):
        nombre= input("Ingrese nombre de departamento:")
        numero_registro= input("Ingrese numero de registro:")
        depa= Empresa(nombre,numero_registro)
        self._departamentos.append(depa)

    def listar_departamentos(self):
        if not self._departamentos:
            print("La lista esta vacia...")
        else:
            for indice,i in enumerate(self._departamentos):
                print(f"{indice}.{i.mostrar_informacion()}")

    def buscar(self):
        buscar_departamento= input("Ingrese departamento a buscar:")
        encontrado = False
        for dep in self._departamentos:
            if dep.nombre ==  buscar_departamento:
                encontrado= True
        if encontrado:
            print(f"Nombre:{self.__nombre}\nNumero Registro:{self.__numero_registro}")

#prueba Clas empleado
empleado= Empleado("01","Pedro Pascal","Jefe de departamento",5000)
empleado.mostrar_informacion()
empleado.modificar_puesto("Asesor")
empleado.mostrar_informacion()
empleado.modificar_salario(5500)
empleado.mostrar_informacion()
empleado.consultar_salario("Pedro Pascal")