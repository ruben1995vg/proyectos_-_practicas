g = {
    'El Sol': 274,
    'Mercurio': 3.7,
    'Venus': 8.87,
    'La Tierra': 9.8,
    'La Luna': 1.62,
    'Marte': 3.71,
    'Jupiter': 24.79,
    'Saturno': 10.44,
    'Urano': 8.87,
    'Neptuno': 11.15,
    'Pluton': 0.62
}
again = 's'


def tiempo(hh, gg):
    i = 0
    i = (2*hh/gg)**(1/2)
    return i


def velocidad_f(gg, hh):
    i = 0
    i = (2*gg*hh)**(1/2)
    return i


while again == 's':

    print('\nEste programa te mostrara el tiempo que tarda en caer un objeto y la velocidad final al care desde la altura que indiques en el planeta que indiques\n')
    print(list(g.keys()))

    g_u = input(
        '\nIngresa el nombre de uno de los cuerpos celestes que aparecen en la parte superior => ').title()
    h_u = int(input(
        '\n ingresa la altura en metros desde la que cae el objeto, ejemplo: 80 => '))

    while g_u not in g.keys():
        print('\n')
        print(list(g.keys()))
        optionU = input(
            '\nAsegúrate de haber ingresado correctamente el nombre de uno de los cuerpos celestes que aparecen en la parte superior => ').title()

    print(
        f'\nEl tiempo que tarda en caer un objeto en {g_u} a una altura de {h_u}m es de: {round(tiempo(h_u, g.get(g_u)),2)}s')
    print(
        f'\nY la velocidad final al care es de: {round(velocidad_f(g.get(g_u), h_u),2)}m/s')
    if g_u != "La Tierra":
        print(
            f"\nen la tierra seria un tiempo: {round(tiempo(h_u, g['La Tierra']),2)}s velocidad: {round(velocidad_f(g['La Tierra'], h_u),2)}m/s")

    again = input('\nsi quieres probar con otro planeta escribe "s" => ')
    print('\n')
    print('\n')
    print('\n')
