import random
#importar librerias para generar numeros aleatorios

def run():

    numero_aleatorio = random.randint(1,100)
         #se genera un numero aleatorio invocando en la variable numero aleatorio
         #la propiedad random.randint que genera cualqueir entero en un rango().
    numero_elegido = int(input("Elige un numero de 1 a 100: "))
        #se convierte a entero el string de numero recibido
    if numero_elegido != range(1, 100):
        print("-------------------------------------------------------")        
        print("Elige una opción correcta.")
        print("-------------------------------------------------------")
        #se genera la logica si el numero elegido es diferente del range para cambiar de opcion.
        #si es numero le dirá si es mayor o menor el emegido, si es texto no lo he solucionado.        
    while numero_elegido != numero_aleatorio:
        #ciclo para que mientras el numero elegido sea diferente al numero aleatorio
        #
        if numero_elegido < numero_aleatorio:

            print("elegiste "+str(numero_elegido)+": Busca un número más grande")
            print("-------------------------------------------------------")
        else:
                print("elegiste "+str(numero_elegido)+": Busca un número más pequeño")
                print("-------------------------------------------------------")

        numero_elegido = int(input("Elige otro número: "))

    print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡Ganaste!!!!!!!!!!!!!!!")
    print(":) :) :) :) :) :) -_- -_- -_- -_- -_- -_-")


if __name__ == "__main__":
    run()