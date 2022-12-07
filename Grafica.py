class graf:

    def __init__(self):
        pass

    def jugar(self):
        import matplotlib.pyplot as plt
        
        opc = "seguir"
        while opc != "salir":
            nombre_1 = input("Ingrese el nombre del primer almuno: ")
            nombre_2 = input("Ingrese el nombre del segundo almuno: ")
            nombre_3 = input("Ingrese el nombre del tercer almuno: ")

            alumnos = [nombre_1, nombre_2, nombre_3]

            cant_notas = int(input("Ingrese la cantidad de notas que desea ingresar por alumno: "))
            promedios = []
        
            for alumno in alumnos:
                print(f"Ingrese las notas del alumno {alumno}: ") 
                acumulador = 0
                notas = []
                for i in range(cant_notas):
                    nota = int(input(f"Nota N°{i+1}: "))
                    while nota < 0 or nota > 10:
                        nota = int(input(f"Nota inválida, vuelva a intentarlo. Nota N°{i+1}: "))

                    notas.append(nota)
                    acumulador += nota
                
                prom = acumulador / cant_notas
                promedios.append(prom)
                print(f"Las notas del alumno {alumno} son {notas}, y su promedio es de {prom}. ")
            
            x = alumnos
            y = promedios

            plt.bar(x, y)
            plt.title("Gráfico de promedios.")
            plt.xlabel("Alumnos.")
            plt.ylabel("Promedios.")
            plt.show()

            opc = input("Gracias por trabajar con nosotros, si desea voler al menú principal ingrese 'salir', de lo contrario presione cualquier tecla: ")