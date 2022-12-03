class dados:

    def __init__(self):
        pass

    def jugar(self):
        import random

        usuario = 0
        computadora = 0
        rondas = 0

        def determinar_ganador(jugador_1, jugador_2):
            if (jugador_1 == jugador_2):
                print (f"Felicidades, elegiste la suma correcta. Tu suma y la de la computadora fue {jugador_1}.")
                return "1"
            else:
                print (f"Lamentablemente no adivinaste la suma. Tu suma fue de {jugador_1} y la de la computadora fue {jugador_2}.")
                return "2"

        def solicitar_jugada_computadora():
            dado_1 = random.choice([1, 2, 3, 4, 5, 6])
            dado_2 = random.choice([1, 2, 3, 4, 5, 6])
            jugada = dado_1 + dado_2

            print (f"La suma de los dados elegidos por la computadora es de: {dado_1} + {dado_2} = {jugada}.")
            return jugada

        def solicitar_jugada_usuario():
            jugada = int(input("Intente adivinar la suma de los dados que lanzará la computadora: "))
            while jugada < 2 or jugada > 12:
                if jugada == "salir":
                    return jugada

                print("Por favor, ingrese un número entre 2 y 12.")
                jugada = int(input("Intente nuevamente: "))
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
            ganador = input("Si desea salir ingrese 'salir', de lo contrarop ingrese 'seguir': ")
            return ganador

        ganador = "seguir"

        while ganador != "salir":
            ganador = jugar()

            if ganador != "salir":
                rondas = rondas + 1

                if ganador == "1":
                    usuario = usuario + 1
                else:
                    computadora = computadora + 1

            ganador = imprimir_marcador()
        
        print ("Juego finalizado.")