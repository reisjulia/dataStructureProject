class Fila:
    def __init__(self):
        self.queue = []

    def add_client(self, client):
        self.queue.append(client)

    def remove_client(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return 'Fila Vazia!'

    def first_client(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return 'Fila Vazia!'

    def size(self):
        return len(self.queue)

    def show(self):
        return print(self.queue)
