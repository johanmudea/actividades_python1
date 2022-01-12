def conversor(tipo_crypto, valor_crypto):
    crypto = input("¿Cuantós " + tipo_crypto + " tienes?:")
    crypto = float(crypto)
    dolares = crypto*valor_crypto
    cop = 4000*dolares
    cop = str(cop)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
    print("Además tienes " + cop + "COP")


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

