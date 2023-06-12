from objects import AdoptSystem, Animal, Client

system = AdoptSystem()

system.animals = [
    Animal('Cachorro', 'Dob').__str__(),
    Animal('Cachorro', 'Husky').__str__(),
    Animal('Cachorro', 'Popo').__str__(),
    Animal('Cachorro', 'Abn').__str__(),
    Animal('Cachorro', 'Ches').__str__(),
    Animal('Cachorro', 'Charles').__str__(),
    Animal('Cachorro', 'Jo').__str__(),
    Animal('Cachorro', 'Ama').__str__()
]

sorted(system.animals)

while True:
    menu_option = int(input('''
    ---- Menu ---- 
    1 - Registrar Animal
    2 - Registrar Cliente
    3 - Buscar Animal de interesse para o cliente
    4 - Exibir Animais
    5 - Exibir Clientes
    6 - Exibir Fila
    7 - Sair
    '''))

    if menu_option == 1:
        system.register_animal()

    elif menu_option == 2:
        system.register_client()

    elif menu_option == 3:
        system.search_queue()

    elif menu_option == 4:
        system.show_animals()

    elif menu_option == 5:
        system.show_clients()

    elif menu_option == 6:
        system.queue.show()

    elif menu_option == 7:
        break

    else:
        print('Invalido!')






