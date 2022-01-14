import random
from typing import Match

def generate_pasword():

    mayus = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
    "R","S","T","U","V","W","X","Y","Z"
    )
    minus = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",
    "r","s","t","u","v","w","x","y","z"
    )
    symbols = ("!", "|", "#", "@", "/", "&", "$", "(",")","=","?","¡","¿")

    numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")

    characters = mayus +  minus + symbols + numbers

    password = []

    for i in range(20):
        random_character = random.choice(characters)
        password.append(random_character)

    password = "".join(password)#el comando "".join pone cada elemento de la lista en 
                                #en una sola palabra
    return password

    
  
  
    



def run():
    password = generate_pasword()
    print("Your new password is: " + password)

if __name__ == "__main__":
    run()