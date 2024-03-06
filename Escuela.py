class Estudiante:
    def __init__(self, nombre="", nota=2, auxencias=0):
        self.nombre = nombre
        self.nota = nota
        self.auxencias = auxencias

    def setNombre(self, nombre):
        self.nombre = nombre

    def setNota(self, nota):
        self.nota = nota

    def setAuxencias(self, auxencias):
        self.auxencias = auxencias

    def getNombre(self):
        return self.nombre

    def getNota(self):
        return self.nota

    def getAuxencias(self):
        return self.auxencias


estudiantes = [Estudiante() for _ in range(500)]
seleccion = 0

while True:
    print()
    print("1. Add estudiante")
    print("2. Eliminar estudiante")
    print("3. Ver estudiante")
    print("4. Salir")
    seleccionSwitch = int(input("Su seleccion: "))

    if seleccionSwitch == 1:
        nombre = input("Inserte el nombre: ")
        nota = int(input("Inserte la nota: "))
        auxencias = int(input("Inserte la cantidad de auxencias: "))

        if seleccion >= 0 and seleccion < 500:
            estudiantes[seleccion].setNombre(nombre)
            estudiantes[seleccion].setNota(nota)
            estudiantes[seleccion].setAuxencias(auxencias)
            seleccion += 1
        else:
            print("La escuela esta llena, elimine un estudiante")

    elif seleccionSwitch == 2:
        if estudiantes[0].getNombre() != "":
            for i in range(seleccion):
                print(f"{i}. {estudiantes[i].getNombre()}")

            EstudianteEliminar = int(input("Seleccione el # del estudiante: "))

            if EstudianteEliminar >= 0 and EstudianteEliminar < 500 and estudiantes[EstudianteEliminar].getNombre() != "":
                for i in range(EstudianteEliminar, 500):
                    estudiantes[i] = Estudiante()
                seleccion -= 1
                print("Estudiante eliminado")
            else:
                print("Estudiante invalido")
        else:
            print("Escuela vacia")

    elif seleccionSwitch == 3:
        if estudiantes[0].getNombre() != "":
            for i in range(seleccion):
                print(f"{i}. {estudiantes[i].getNombre()}")

            NumeroEstudiante = int(input("Seleccione el numero del estudiante: "))

            if NumeroEstudiante >= 0 and NumeroEstudiante < 500:
                if estudiantes[NumeroEstudiante].getNombre() != "":
                    print("Estudiante:", estudiantes[NumeroEstudiante].getNombre())
                    print("Nota:", estudiantes[NumeroEstudiante].getNota())
                    print("Auxencias:", estudiantes[NumeroEstudiante].getAuxencias())
                    print("Sugerencias:")

                    if estudiantes[NumeroEstudiante].getNota() < 5:
                        print("Se pueden mejorar las notas")

                    if estudiantes[NumeroEstudiante].getAuxencias() > 3:
                        print("Se puede mejorar la asistencia")
                else:
                    print("Estudiante invalido")
            else:
                print("Estudiante invalido")
        else:
            print("Escuela vacia, inserte un estudiante")

    elif seleccionSwitch == 4:
        print("Gracias por usar")
        break

    else:
        print("Opcion invalida")
