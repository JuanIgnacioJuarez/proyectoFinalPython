class adiNum:

    def __init__(self):
        pass

    def jugar(self):
        import random

        usuario = 0
        computadora = 0
        rondas = 0

        def determinar_ganador(jugador_1, jugador_2):
            if (jugador_1 == jugador_2):
                print(f"Felicidades, elegiste el número correcto. Tu número y el de la computadora fue {jugador_1}.")
                return "1"
            else:
                print(f"Lamentablemente no elegiste el número correcto. Tu número fué {jugador_1} y el de la computadora fue {jugador_2}.")
                return "2"

        def solicitar_jugada_usuario():
            jugada = input("Ingrese un número del 1 al 5 intentando adivinar cual es el que eligira la computadora. Si desea salir escriba 'salir'. ")
            while jugada != "1" and jugada != "2" and jugada != "3" and jugada != "4" and jugada != "5":
                if jugada == "salir":
                    return jugada

                print ("Por favor, ingrese un número entre el 1 y el 5.")
                jugada = input("Ingrese un número del 1 al 5 intentando adivinar cual es el que eligira la computadora. Si desea salir escriba 'salir'.")
            return jugada

        def solicitar_jugada_computadora():
            jugada = random.choice(["1", "2", "3", "4", "5"])
            print (f"Computadora: {jugada}")
            return jugada

        def jugar():
            usuario = solicitar_jugada_usuario()
            if usuario == "salir":
                return usuario

            computadora = solicitar_jugada_computadora()
            ganador = determinar_ganador(jugador_1 = usuario, jugador_2 = computadora)
            return ganador

        def imprimir_marcador():
            print("\n=================================")
            print("Rondas jugadas:", rondas)
            print("Victorias usuario:", usuario)
            print("Victorias computadora:", computadora)
            print("=================================\n")

        ganador = "seguir"
        
        while ganador != "salir":
            ganador = jugar()

            if ganador != "salir":
                rondas = rondas + 1

                if ganador == "1":
                    usuario = usuario + 1
                else:
                    computadora = computadora + 1

            imprimir_marcador()
        
        print("Juego finalizado.")