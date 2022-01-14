

objeto = ["hola mundo", 1, 3, [1,2,3,[1,3,5],5] ]
print("---------------------")
print(objeto)
print("---------------------")

for element in objeto:
    print(element)
    print("----------------------")
 
objeto.append("chao mundo")

print(objeto)
print("----------------------")

objeto.pop(3)

print(objeto)

print("----------------------")

print(objeto[::-1])

print("----------------------")

for element in objeto:
    print(element)
    print("----------------------")


print(objeto[0:5:2])
