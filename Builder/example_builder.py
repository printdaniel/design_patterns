""" 
El patrón de diseño Builder es un patrón de creación que se utiliza para crear 
objetos complejos con muchos atributos o partes interdependientes. En lugar de 
tener un constructor con muchos argumentos, el patrón Builder divide la 
construcción del objeto en etapas separadas y separa la lógica de construcción 
de la lógica de uso del objeto.

En Python, el patrón Builder se puede implementar de varias maneras. Una de las 
formas más comunes de implementar el patrón Builder es a través de una clase 
llamada Builder que se encarga de definir los métodos necesarios para construir 
el objeto y una clase llamada Director que se encarga de usar la clase Builder 
para crear el objeto.
"""

class Pizza:
    def __init__(self, dough, sauce, topping):
        self.dough = dough
        self.sauce = sauce
        self.topping = topping
        
class PizzaBuilder:
    def build_dough(self):
        pass
    
    def build_sauce(self):
        pass
    
    def build_topping(self):
        pass
    
    def get_pizza(self):
        return Pizza(self.build_dough(), self.build_sauce(), self.build_topping())

class MargheritaPizzaBuilder(PizzaBuilder):
    def build_dough(self):
        return "thin"
    
    def build_sauce(self):
        return "tomato"
    
    def build_topping(self):
        return "mozzarella"
    
class PepperoniPizzaBuilder(PizzaBuilder):
    def build_dough(self):
        return "thick"
    
    def build_sauce(self):
        return "tomato"
    
    def build_topping(self):
        return "mozzarella, pepperoni"

class PizzaMaker:
    def __init__(self, builder):
        self._builder = builder
    
    def make_pizza(self):
        return self._builder.get_pizza()

pizza_maker = PizzaMaker(MargheritaPizzaBuilder())
margherita_pizza = pizza_maker.make_pizza()

pizza_maker = PizzaMaker(PepperoniPizzaBuilder())
pepperoni_pizza = pizza_maker.make_pizza()
