nombre = "francisco"
print(nombre)

#nombre[0] llama al primero elemento del string,
#en este caso el 0 denota el principio. 
print(nombre[0])
#nombre[4] llama al quinto elemento del string,
#ya que se comienza a contar desde 0. 
print(nombre[4])
#nombre[:4] recorres desde la posicion cero hasta la 4
#se puede poner el cero de esta forma [0:x] 
print(nombre[:4])
#equivalente pero comenzando desde el indicado y terminando en el final.
print(nombre[3:])
#Entre las posiciones indicadas
print(nombre[2:6])
#el valor agregado al final indica el "paso" que se le da.
print(nombre[1:7:2])
#devuelve la lista de caracteres alrevez.
print(nombre[::-1])