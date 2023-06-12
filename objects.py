from fila import Fila


class Animal:
    def __init__(self, type, race):
        self.type = type
        self.race = race

    def __str__(self):
        return f'{self.race}'


class Client:
    def __init__(self, user, phone_number, interested_race):
        self.user = user
        self.phone_number = phone_number
        self.interested_race = interested_race

    def __str__(self):
        return f'{self.user}'


def animals_binary_search(animals, searched_type):
    left = 0
    right = len(animals) - 1

    while left <= right:
        mid = (left + right) // 2

        if animals[mid] == searched_type:
            return animals[mid]
        elif animals[mid] < searched_type:
            left = mid + 1
        else:
            right = mid - 1

    return print('Not Found!')


class AdoptSystem:
    def __init__(self):
        self.animals = []
        self.clients = []
        self.queue = Fila()

    def show_clients(self):
        return print(self.clients)

    def show_animals(self):
        return print(self.animals)

    def register_client(self):
        client = Client('username', 'phone_number', 'interested_race')
        client.user = str(input('Username: '))
        client.phone_number = str(input('Phone Number: '))
        client.interested_race = str(input('Interested Race: '))
        self.queue.add_client(client)
        self.clients.append(client.__str__())

    def register_animal(self):
        animal = Animal('type', 'race')
        animal.type = str(input('Tipo: '))
        animal.race = str(input('Raça: '))
        return self.animals.append(animal.__str__())

    def search_queue(self):
        try:
            client = self.queue.first_client()
            search = animals_binary_search(sorted(self.animals), client.interested_race)
            if search:
                print(f"Encontramos um {search}.")
                return self.queue.remove_client()
            return self.queue.remove_client()
        except:
            print('Sem clientes na fila!')
