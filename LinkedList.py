class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, initial_elements=[]):
        self.head = None
        self.size = 0

        # si me mandan una lista inicial la recorro
        for value in initial_elements:
            self.append(value)


    def __str__(self):
        current = self.head
        text = ""

        while current != None:
            text = text + str(current.data)
            if current.next != None:
                text = text + " -> "
            current = current.next

        if text == "":
            return "Vacio"
        else:
            return text


    def __len__(self):
        return self.size


    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("El idice no existe")

        current = self.head
        contador = 0

        while contador < index:
            current = current.next
            contador = contador + 1

        return current.data


    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False


    def __iter__(self):
        current = self.head
        while current != None:
            yield current.data
            current = current.next


    def __contains__(self, element):
        current = self.head

        while current != None:
            if current.data == element:
                return True
            current = current.next

        return False


    def append(self, element):
        new_node = Node(element)

        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node

        self.size = self.size + 1


    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("El indice no existe")

        new_node = Node(element)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            contador = 0

            while contador < index - 1:
                current = current.next
                contador = contador + 1

            new_node.next = current.next
            current.next = new_node

        self.size = self.size + 1


    def remove(self, element):
        if self.head == None:
            raise ValueError("El elemento no existe")

        if self.head.data == element:
            self.head = self.head.next
            self.size = self.size - 1
            return

        current = self.head

        while current.next != None:
            if current.next.data == element:
                current.next = current.next.next
                self.size = self.size - 1
                return
            current = current.next

        raise ValueError("El elemento no existe")


    def pop(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("El indice no existe")

        current = self.head

        if index == 0:
            value = self.head.data
            self.head = self.head.next
        else:
            contador = 0
            while contador < index - 1:
                current = current.next
                contador = contador + 1

            value = current.next.data
            current.next = current.next.next

        self.size = self.size - 1
        return value


    def clear(self):
        self.head = None


# PRUEBA EN TERMINAL

lista = LinkedList([1, 2, 3])

print("Lista inicial:")
print(lista)

lista.append(4)
print("Después de append(4):")
print(lista)

lista.insert(1, 10)
print("Después de insert(1, 10):")
print(lista)

lista.remove(2)
print("Después de remove(2):")
print(lista)

print("Elemento en índice 2:")
print(lista[2])

print("Pop en índice 0:")
print(lista.pop(0))

print("Lista final:")
print(lista)

print("¿Está vacío?")
print(lista.isEmpty())

print("Tamaño:")
print(len(lista))
        self.size = 0