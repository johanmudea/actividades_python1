def palindromo(palabra):
    palabra=palabra.replace(" ","")
    palabra=palabra.lower()
    palabra_invertida = palabra [::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False
#la funcion definida lo que hace es tomar una palabra y y luego quitar espacios y
#ponerla toda minuscula la compara con la misma palabra escrita alrevez y de esta forma
#encontrar si es palindromo o no, es decir que se escriben igual en ambos sentidos.
def run():#es una buena practica definir una función para comenzar a programar.
    palabra = input("ingrese una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("es palindromo")
    else:
        print("no es palindromo")

if __name__ == '__main__':#es una buena practica y lanza la función del programa.
    run()