import PiedraPapelTijera
import AdivinarNum
import Dados
import Grafica

nombre = input("Ingrese su nombre: ")

print(f"Hola {nombre}, bienvenido.")

opc = 1

while opc != 5:
    print("1. Juego de Piedra Papel o Tijera.")
    print("2. Juego de adivinar el número.")
    print("3. Juego de adivinar la suma de dos dados.")
    print("4. Ingresar una función para luego ser graficada.")
    print("5. Salir.")
    opc = int(input("Ingrese el número de opción de lo que desee hacer: "))
    if opc < 1 or opc > 5:
        print("Opción inválida, vuelva a intentarlo.")
    else:
        if opc == 1:
            juego = PiedraPapelTijera.PPT()
            juego.jugar()
        elif opc == 2:
            juego = AdivinarNum.adiNum()
            juego.jugar()
        elif opc == 3:
            juego = Dados.dados()
            juego.jugar()
        elif opc == 4:
            juego = Grafica.graf()
            juego.jugar()
        

print(f"Gracias {nombre} por jugar con nosotros.")