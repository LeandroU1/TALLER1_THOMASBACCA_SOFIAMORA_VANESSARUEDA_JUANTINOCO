class OrderList:

    def __init__(self, initial_elements=[]):
        self.data = []

        for element in initial_elements:
            self.add(element)


    def __str__(self):
        if len(self.data) == 0:
            return "Empty"

        text = ""
        i = 0

        while i < len(self.data):
            text = text + str(self.data[i])
            if i != len(self.data) - 1:
                text = text + " -> "
            i = i + 1

        return text


    def __len__(self):
        return len(self.data)


    def __getitem__(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("El idice no existe")

        return self.data[index]


    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False


    def __iter__(self):
        i = 0
        while i < len(self.data):
            yield self.data[i]
            i = i + 1


    def __contains__(self, element):
        for value in self.data:
            if value == element:
                return True
        return False


    def add(self, element):
        if len(self.data) == 0:
            self.data.append(element)
            return

        i = 0

        while i < len(self.data) and self.data[i] < element:
            i = i + 1

        self.data.insert(i, element)


    def remove(self, element):
        if element not in self.data:
            raise ValueError("El elemento no existe")
        self.data.remove(element)


    def pop(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("El idice no existe")

        return self.data.pop(index)


    def clear(self):
        self.data = []

lista = OrderList()

print("Lista inicial:")
print(lista)

lista.add(5)
lista.add(2)
lista.add(8)
lista.add(1)

print("Después de agregar 5, 2, 8, 1 (orden automático) :D :")
print(lista)

print("Tamaño de la lista:")
print(len(lista))

print("Elemento en índice 2:")
print(lista[2])

print("¿Existe el 5 en la lista?")
print(5 in lista)

lista.remove(2)
print("Después de eliminar 2:")
print(lista)

print("Pop en índice 1:")
print(lista.pop(1))

print("Lista final:")
print(lista)