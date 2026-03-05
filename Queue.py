class Queue:
    
    def __init__(self, initial_elements=[]):
        self.data = []

        for element in initial_elements:
            self.push(element)


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


    def isEmpty(self):
        return len(self.data) == 0


    def peek(self):
        if self.isEmpty():
            return None
        
        return self.data[0]


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


    def push(self, element):
        self.data.append(element)


    def pop(self, index=None):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        
        return self.data.pop(0)
    
cola = Queue()

print("Cola inicial:")
print(cola)

cola.push(10)
cola.push(20)
cola.push(30)

print("Despues de push 10, 20, 30:")
print(cola)

print("Siguiente elemento (peek):")
print(cola.peek())

print("Pop:")
print(cola.pop())

print("Cola despues de pop:")
print(cola)

print("Tamaño de la cola:")
print(len(cola))

print("¿Existe el 20 en la cola?")
print(20 in cola)