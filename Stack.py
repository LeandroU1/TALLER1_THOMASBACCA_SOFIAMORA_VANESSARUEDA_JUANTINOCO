class Stack:
    
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
        
        return self.data[len(self.data) - 1]
    

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
            raise IndexError("Stack is empty")
        
        return self.data.pop()

pila = Stack()

print("Pila inicial:")
print(pila)

pila.push(10)
pila.push(20)
pila.push(30)

print("Despues de push 10, 20, 30:")
print(pila)

print("Elemento en el tope (peek):")
print(pila.peek())

print("Pop:")
print(pila.pop())

print("Pila despues de pop:")
print(pila)

print("Tamaño de la pila:")
print(len(pila))

print("¿Existe el 10 en la pila?")
print(10 in pila)