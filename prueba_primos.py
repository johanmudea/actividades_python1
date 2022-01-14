#la funcoin es primo tomará el numero.
#con un ciclo entre el numero 1 y el numero elegido se evaluará el modulo


def es_primo(numero):
    contador = 0
    for i in range (1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
            #contador = contador + 1
    if contador == 0:
        return True
    else:
        return False
        


#definir funcion run y recibir el parametro numero del user, si al pasar el 
#el parametro por la función es primo, imprime en pantalla, si no, también.
def run():
    numero = int(input("escribe un número: "))
    if es_primo(numero):
        print("es primo")
    else:
        print("no es primo")
        

if __name__ == "__main__":
    run()
