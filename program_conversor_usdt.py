def conversor(tipo_crypto, valor_crypto):
    dolares = input("¿Cuantós dolares tienes?:")
    dolares = float(dolares)
    crypto = dolares/valor_crypto
    crypto = str(crypto)
    print("Tienes " + crypto +" "+tipo_crypto)



menu = """"BIENVENIDO AL CONVERSOR CRYPTO 
DE LAS 3 PRINCIPALES COINS DEL MERCADO

1 - BITCOIN
2 - ETHEREUM
3 - SOLANA

ELIGE UNA OPCIÓN:  """

opcion = int(input(menu)) 

print(opcion)

if opcion == 1:
    conversor("BTC", 40000)
elif opcion == 2:
    conversor("ETH", 3000)
elif opcion == 3:
    conversor("SOL", 140) 
else:
    print("Ingrese una opción correcta por favor")

