from abc import ABC, abstractmethod

# Componente base del patrón Composite
class Component(ABC):
    @abstractmethod
    def operate(self):
        pass

# Componente hoja que realiza una operación aritmética simple
class Leaf(Component):
    def _init_(self, value):
        self.value = value
    
    def operate(self):
        return self.value

# Componente compuesto que contiene uno o más componentes hoja o compuestos
class Composite(Component):
    def _init_(self, operation, *components):
        self.operation = operation
        self.components = components
    
    def operate(self):
        if self.operation == '+':
            return sum(component.operate() for component in self.components)
        elif self.operation == '-':
            return self.components[0].operate() - self.components[1].operate()
        elif self.operation == '*':
            return self.components[0].operate() * self.components[1].operate()
        elif self.operation == '/':
            return self.components[0].operate() / self.components[1].operate()
        else:
            raise ValueError(f"Invalid operation: {self.operation}")

# Ejemplo de uso
if _name_ == '_main_':
    # Se crea una estructura de operaciones aritméticas
    tree = Composite('+',
                     Composite('-',
                               Leaf(10),
                               Leaf(5)),
                     Composite('*',
                               Leaf(3),
                               Leaf(4)))
    
    # Se realiza la operación
    result = tree.operate()
    print(result)  # Output: 22
