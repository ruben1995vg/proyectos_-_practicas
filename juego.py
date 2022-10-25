import getpass
import random

opciones = {1: 'Piedra', 2: 'Papel', 3: 'Tijera'}


def tex():
    print(f'\nHas elegido: {opciones.get(usuario)}')
    print(f'El PC ha elegido: {opciones[pc]}\n')


print('\njuego de Piedra, Papel o Tijera \n')
usuario = int(
    input('ingrese: \n1 para Piedra \n2 para Papel \n3 para Tijera => '))
pc = random.randint(1, 3)
if pc == usuario:
    tex()
    print('Empate')
elif (usuario == 1 and pc == 3) or (usuario == 2 and pc == 1) or (usuario == 3 and pc == 2):
    tex()
    print('Has ganado')
elif usuario not in range(1, 3):
    tex()
    print('Has perdido')
else:
    tex()
    print('Has perdido')

getpass.getpass('press enter')
