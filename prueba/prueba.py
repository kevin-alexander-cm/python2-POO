from datetime import date

class Persona:

    def __init__(self, run, nombre, direccion, sexo, fechaNacimiento):
        self.run = run
        if len(self.run) < 7:
            self.run = "11111-1"
        self.nombre = nombre
        if len(self.nombre) < 3:
            self.nombre = "Juan por defecto"
        self.direccion = direccion
        self.sexo = sexo
        self.fechaNacimiento = fechaNacimiento
        if self.fechaNacimiento > date.today():
            print("La fecha del alumno no debe ser mayor a hoy")


    def getRut(self):
        return self.run

    def getNombre(self):
        return self.nombre

    def getDireccion(self):
        return self.direccion

    def getSexo(self):
        return self.sexo

    def getFechaNacimiento(self):
        return self.fechaNacimiento

    def setNombre(self, nombre):
        self.nombre = nombre

    def setDireccion(self, direccion):
        self.direccion = direccion

    def setSexo(self, sexo):
        self.sexo = sexo

    def setFechaNacimiento(self, fechaNacimiento):
        self.fechaNacimiento = fechaNacimiento

    def mostrarDatos(self):
        return f"{self.getRut()} {self.getNombre()} {self.getDireccion()} {self.getSexo()} {self.getFechaNacimiento()}"


class Alumno(Persona):

    def __init__(self, run, nombre, direccion, sexo, fechaNacimiento, fechaRegistro, codigoAlumno):
        super().__init__(run, nombre, direccion, sexo, fechaNacimiento)
        self.fechaRegistro = fechaRegistro
        if self.fechaRegistro > date.today():
            print("La fecha del alumno no debe ser mayor a hoy")
        self.codigoAlumno = codigoAlumno
        if self.codigoAlumno < 5000:
            self.codigoAlumno = 5000

    def getFechaResgistro(self):
        return self.fechaRegistro


class Funcionario(Persona):

    def __init__(self, run, nombre, direccion, sexo, fechaNacimiento, fechaIngreso, sueldo, campus):
        super().__init__(run, nombre, direccion, sexo, fechaNacimiento)
        # self.codigoAsignatura = codigoAsignatura
        # self.profesor = profesor
        # self.listaAlumnos = listaAlumnos
        self.fechaIngreso = fechaIngreso
        if self.fechaIngreso > date.today():
            print("La fecha del alumno no debe ser mayor a hoy")
        self.sueldo = sueldo
        if self.sueldo < 300000:
            self.sueldo = 300000
        self.campus = campus

    def getFechaIngreso(self):
        return self.fechaIngreso

    def getSueldo(self):
        return self.sueldo

    def setSueldo(self, sueldo):
        self.sueldo = sueldo

    def recalcularSueldo(self):
        self.sueldo += self.sueldo * 0.05
        return self.sueldo

    def mostrarDatos(self):
        return super().mostrarDatos() + f"{self.fechaIngreso} {self.sueldo} {self.campus}"


class Titulo:

    def __init__(self, nombreProfesor, fechaTitulacion):
        self.nombreProfesor = nombreProfesor
        self.fechaTitulacion = fechaTitulacion

    def getNombreProfesor(self):
        return self.nombreProfesor

    def getFechaTitulacion(self):
        return self.fechaTitulacion


class Docente(Funcionario):

    def __init__(self, run, nombre, direccion, sexo, fechaNacimiento, fechaIngreso, sueldo, campus, titulo=None):
        super().__init__(run, nombre, direccion, sexo, fechaNacimiento, fechaIngreso, sueldo, campus)
        self.profesion = titulo
        # por defecto
        if self.profesion is None:
            self.profesion = Titulo(self.nombre, date.today())

    def getProfesion(self):
        return self.profesion

    def setProfesion(self, titulo):
        self.profesion = titulo

    def mostrarDatos(self):
        return super().mostrarDatos() + f"{self.profesion}"


class Administrativo(Funcionario):

    def __init__(self, run, nombre, direccion, sexo, fechaNacimiento, fechaIngreso, sueldo, campus, cargo):
        super().__init__(run, nombre, direccion, sexo, fechaNacimiento, fechaIngreso, sueldo, campus)
        self.cargo = cargo
        if len(self.cargo) < 5:
            self.cargo = "Cargo Temporal"

    def getCargo(self):
        return self.cargo

    def setCargo(self, cargo):
        self.cargo = cargo

    def mostrarDatos(self):
        return super().mostrarDatos() + f"{self.cargo}"



class Sede:

    def __init__(self, nombre, direccion, listaFuncionarios):
        self.nombre = nombre
        if len(self.nombre) < 6:
            self.nombre = "Sede Centro"
        self.direccion = direccion
        self.listaFuncionarios = listaFuncionarios

    def getNombre(self):
        return self.nombre

    def getDireccion(self):
        return self.direccion

    def setNombre(self, nombre):
        self.nombre = nombre

    def setDireccion(self, direccion):
        self.direccion = direccion

    def getListaFuncionarios(self):
        return self.listaFuncionarios


class Asignatura:

    def __init__(self, codigoAsignatura, profesor, listaAlumnos):
        self.codigoAsignatura = codigoAsignatura
        self.profesor = profesor
        self.listaAlumnos = listaAlumnos

    def getProfesor(self):
        return self.profesor

    def getCodigo(self):
        return self.codigoAsignatura

    def setProfesor(self, profesor):
        self.profesor = profesor

    def matricularAlumno(self, alumno):
        self.listaAlumnos.append(alumno)
        return True