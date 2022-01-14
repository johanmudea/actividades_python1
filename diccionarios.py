""" 
#que es una tupla?, es una lista que no se puede agregar ni quitar información.

tuplita = (1, 2, 3, 4 , 6, 7, 8)

print(tuplita)

print (tuplita[::-1] )

for element in tuplita:
     print(element) """

  my_dictionary = {"name":"johan", "age": 30, "gender": "male"}

    countries_population = {
    "argentina" : 45000000,
    "colombia" : 50000000,
    "brasil" : 250000000,}

    print("------------------------------------------")

    print(my_dictionary)

    print("------------------------------------------")

    print("su nombre es "+ str(my_dictionary["name"]))

    print("------------------------------------------")


    print("su edad es "+ str(my_dictionary["age"])+" años")

    print("------------------------------------------")

    print("su genero es "+ str(my_dictionary["gender"])+"")

    print("------------------------------------------")

    for elementos in my_dictionary.keys():
        print(elementos)

        print("------------------------------------------")

    for elementos in my_dictionary.values():
        print(elementos)
        print("------------------------------------------")

    for elementos in countries_population.values():
        print(elementos)
        print("------------------------------------------")

