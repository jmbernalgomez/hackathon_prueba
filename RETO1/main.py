import time
from time import sleep
import random

op = ['piedra', 'papel', 'tijeras']
sep = "-------------------------------------------"

while True:
    user = input("Elige (piedra, papel o tijeras):").lower()
    sleep(0.9)
    if user not in op:
        print ("Movimiento no válido")
        continue
    pc = random.choice(op)
    sleep(0.9)
    print(f"\n La máquina ha elegido: {pc}")
    sleep(0.9)
    if user == pc:
        print(f"EMPATE")
    elif user == "piedra" and pc == "tijeras":
        print(f"\nGANASTE !! {user} gana a {pc}")
    elif user == "tijeras" and pc == "papel":
        print(f"\nGANASTE !! {user} gana a {pc}")
    elif user == "papel" and pc == "piedra":
        print(f"\nGANASTE !! {user} gana a {pc}")
    else:
        print(f"\nPERDISTE !! {pc} gana a {user}")
    sleep(0.9)
    print(f"{sep}FIN{sep}")