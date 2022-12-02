class PPT:
    
    def __init__(self):
        pass

    def jugar(self):
    
        import random

        victorias_usuario = 0
        victorias_computadora = 0
        empates = 0
        rondas = 0

        def determinar_ganador(jugador_1, jugador_2):
            if ((jugador_1 == "piedra" and jugador_2 == "tijera") or
                (jugador_1 == "papel" and jugador_2 == "piedra") or
                (jugador_1 == "tijera" and jugador_2 == "papel")):

                print("Usuario le gana a Computadora ya que", jugador_1, "le gana a", jugador_2)
                return "1"

            elif ((jugador_2 == "piedra" and jugador_1 == "tijera") or
                (jugador_2 == "papel" and jugador_1 == "piedra") or
                (jugador_2 == "tijera" and jugador_1 == "papel")):

                print("Computadora le gana a Usuario ya que", jugador_2, "le gana a", jugador_1)
                return "2"

            elif ((jugador_1 == "piedra" or jugador_1 == "papel" or jugador_1 == "tijera") 
                and jugador_1 == jugador_2):
                print("Usuario empata con Computadora ya que", jugador_1, "empata con", jugador_2)
                return "empate"
            else:
                print("Jugada invalida")
                return "invalido"

        def solicitar_jugada_usuario():
            jugada = input("Ingrese piedra/papel/tijera. Si desea salir escriba 'salir': ")
            while jugada != "piedra" and jugada != "papel" and jugada != "tijera":

                if jugada == "salir":
                    break

                print("Por favor ingrese una jugada valida.")
                jugada = input("Ingrese piedra/papel/tijera. Si desea salir escriba 'salir': ")

            return jugada

        def obtener_jugada_computadora():
            jugada = random.choice(["piedra", "papel", "tijera"])
            print("Computadora:", jugada)

            return jugada

        def jugar():
            usuario = solicitar_jugada_usuario()
            if usuario == "salir":
                return usuario

            computadora = obtener_jugada_computadora()
            ganador = determinar_ganador(jugador_1=usuario, jugador_2=computadora)

            return ganador

        def imprimir_marcador():
            print("\n=================================")
            print("Rondas jugadas:", rondas)
            print("Victorias usuario:", victorias_usuario)
            print("Victorias computadora:", victorias_computadora)
            print("Empates:", empates)
            print("=================================\n")


        ganador = "seguir"
        while ganador != "salir":
            ganador = jugar()

            if ganador != "salir":
                rondas = rondas + 1

                if ganador == "1":
                    victorias_usuario += 1
                elif ganador == "2":
                    victorias_computadora += 1
                elif ganador == "empate":
                    empates += 1

            imprimir_marcador()

        print("Juego finalizado.")