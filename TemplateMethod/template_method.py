from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        self.base_operation1()
        self.required_operation()
        self.base_operation2()

    def base_operation1(self):
        print("Operación base 1")

    def base_operation2(self):
        print("Operación base 2")

    @abstractmethod
    def required_operation(self):
        pass

class ConcreteClass(AbstractClass):
    def required_operation(self):
        print("Operación requerida implementada en la subclase")

if __name__ == "__main":
    concrete = ConcreteClass()
    concrete.template_method()
