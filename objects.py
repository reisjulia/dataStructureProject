class Animal:
    def __init__(self, race, color, age, animal_port, particularity):
        self.race = race
        self.age = age
        self.color = color
        self.animal_port = animal_port
        self.particularity = particularity


class Canine(Animal):
    def __init__(self, race, color, age, animal_port, particularity):
        super().__init__(race, color, age, animal_port, particularity)


class Feline(Animal):
    def __init__(self, race, color, age, animal_port, particularity):
        super().__init__(race, color, age, animal_port, particularity)


class Client:
    def __init__(self, first_name, last_name, cpf):
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class AdoptSystem:
    def __init__(self):
        self.animals = []
        self.clients = []

    def show_clients(self):
        return print(self.clients)

    def register_client(self, first_name, last_name, cpf):
        client = Client(first_name, last_name, cpf)
        self.clients.append(client.__str__())
