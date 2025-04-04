### Variables globales y constantes ###

### Librerías ###

import menu

### Funciones ###

### Variables locales ###

trigger = True
option = ''

### Programa Principal ###

while trigger:
    menu.menu_principal()

    option = input(f'\nIntroduce una opción del menu: ')

    match option:

        case '1': 
            menu.menu_productos()

        case '2': 
            menu.menu_clientes()

        case '3': 
            menu.menu_pedidos()

        case '4': 
            menu.menu_reseñas()

        case '5': 
            print(f'\n¡¡¡GRACIAS POR UTILIZAR NUESTRO PROGRAMA!!!')
            trigger = False

        case _: 
            input(f'\n¡¡¡Opción incorrecta!!!\nPulsa ENTER para continuar...')
