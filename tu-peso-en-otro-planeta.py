from ast import keyword
from pydoc import plainpager


cuerposCelestes = {
    'Sol': 274,
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

again = 'si'

while again == 'si':

    print('\nEste programa te mostrara tu peso en el planeta que selecciones de la lista inferior\n')
    print(list(cuerposCelestes.keys()))

    optionU = input(
        '\nIngresa el nombre de uno de los cuerpos celestes que aparecen en la parte superior => ').title()
    pesoU = float(input('\nIngresa tu peso actual => '))
    resultado = 0.0

    while optionU not in cuerposCelestes.keys():
        print('\n')
        print(list(cuerposCelestes.keys()))
        optionU = input(
            '\nAsegúrate de haber ingresado correctamente el nombre de uno de los cuerpos celestes que aparecen en la parte superior => ').title()

    resultado = round(
        (pesoU/cuerposCelestes['La Tierra'])*cuerposCelestes.get(optionU), 2)
    print(f'\nTu peso en {optionU} es de: {resultado} Kg')

    again = input('\nsi quieres probar con otro planeta escribe "si" => ')
    print('\n')
    print('\n')
    print('\n')
