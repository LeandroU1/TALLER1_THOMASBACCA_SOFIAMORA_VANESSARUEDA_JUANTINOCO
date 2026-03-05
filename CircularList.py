class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularList:
    
    def __init__(self, initial_elements=[]):
        self.head = None
        self.size = 0

        for element in initial_elements:
            self.append(element)


    def __str__(self):
        if self.head == None:
            return "Empty"

        text = ""
        current = self.head
        count = 0

        while count < self.size:
            text = text + str(current.data)
            if count != self.size - 1:
                text = text + " -> "
            current = current.next
            count = count + 1

        return text


    def __len__(self):
        return self.size


    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index does not exist")

        current = self.head
        count = 0

        while count < index:
            current = current.next
            count = count + 1

        return current.data


    def isEmpty(self):
        return self.size == 0


    def __iter__(self):
        current = self.head
        count = 0

        while count < self.size:
            yield current.data
            current = current.next
            count = count + 1


    def __contains__(self, element):
        current = self.head
        count = 0

        while count < self.size:
            if current.data == element:
                return True
            current = current.next
            count = count + 1

        return False


    def append(self, element):
        new_node = Node(element)

        if self.head == None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head

            while current.next != self.head:
                current = current.next

            current.next = new_node
            new_node.next = self.head

        self.size = self.size + 1


    def add(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("Index does not exist")

        new_node = Node(element)

        if index == 0:
            if self.head == None:
                self.head = new_node
                new_node.next = self.head
            else:
                current = self.head

                while current.next != self.head:
                    current = current.next

                new_node.next = self.head
                current.next = new_node
                self.head = new_node
        else:
            current = self.head
            count = 0

            while count < index - 1:
                current = current.next
                count = count + 1

            new_node.next = current.next
            current.next = new_node

        self.size = self.size + 1


    def remove(self, element):
        if self.head == None:
            raise ValueError("Element does not exist")

        current = self.head
        prev = None
        count = 0

        while count < self.size:
            if current.data == element:

                if prev == None:
                    last = self.head
                    while last.next != self.head:
                        last = last.next

                    self.head = self.head.next
                    last.next = self.head
                else:
                    prev.next = current.next

                self.size = self.size - 1
                return

            prev = current
            current = current.next
            count = count + 1

        raise ValueError("Element does not exist")


    def pop(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index does not exist")

        current = self.head
        prev = None
        count = 0

        while count < index:
            prev = current
            current = current.next
            count = count + 1

        value = current.data

        if prev == None:
            last = self.head
            while last.next != self.head:
                last = last.next

            self.head = self.head.next
            last.next = self.head
        else:
            prev.next = current.next

        self.size = self.size - 1

        return value


    def clear(self):
        self.head = None
        self.size = 0

lista = CircularList()

print("Lista inicial:")
print(lista)

lista.append(10)
lista.append(20)
lista.append(30)

print("Despues de append:")
print(lista)

lista.add(1, 15)

print("Despues de add en posicion 1:")
print(lista)

lista.remove(20)

print("Despues de remove 20:")
print(lista)

print("Pop indice 1:")
print(lista.pop(1))

print("Lista final:")
print(lista)

print("Tamaño:")
print(len(lista))