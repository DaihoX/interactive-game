import time
import sys
import variables

def mostrar_menu():
    print("\n--- Bienvenido a Corona de Hielo---")
    print("Corona de Hielo es una aventura interactiva de puzzles")
    print("1. Iniciar una nueva partida")
    print("2. Cargar partida")
    print("3. Historia")
    print("4. Salir")

def escribir_poco_a_poco(texto = variables.msg , retraso=0.1):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()  # Asegura que se imprima el carácter inmediatamente
        time.sleep(retraso)  # Tiempo de retraso entre cada carácter
    print()  # Añade un salto de línea al final    
    
class main():

    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")

        if opcion == "1":
            #iniciar partida
            print("\nTe despiertas de la nada, te duelen los ojos y todo esta oscuro. No recuerdas como llegaste aqui \n")
            print("\nSolo puedes ver 3 luces enfrente tuyo, ¿que deseas hacer? \n")

        elif opcion == "2":
            #Cargar una partida de los 3 slots de guardado
            opcion2 = input("Seleccione se partida")
            if opcion2 == "1":
                print("Cargando partida")
            elif opcion2 == "2":
                print("Cargando partida")
            elif opcion2 == "3":
                print("Cargando partida")
        elif opcion == "3":
            #Por terminar, idea generar una cadena texto que se imprima poco a poco con al rededor de 0.1 segundos entre caracter para dar un estilo visual mas limpio 
            #Iniciar historia y volver al menu
            escribir_poco_a_poco()

        elif opcion == "4":
            #Terminar ejecucion de el juego
            print("Gracias por jugar")
            sys. exit()

        else:
            print("Opción no válida. Inténtelo de nuevo.")

mostrar_menu()