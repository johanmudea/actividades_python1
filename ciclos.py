def run():
    name = input("escribe tu nombre: ")
    for letter in name:
        print(letter)

    frase = input("Escribe una frase: ")
    for caracter in frase:
        print(caracter.upper())


if __name__=="__main__":
    run()
