""" 
El patrón de diseño Factory es un patrón de creación que proporciona una 
interfaz para la creación de objetos en una clase o un grupo de clases 
relacionadas sin especificar exactamente la clase que se creará. En lugar de 
utilizar new operator directamente para crear objetos, el patrón Factory define 
una interfaz para crear un objeto, pero permite a las subclases decidir qué 
clase de objeto crear. Esto permite a la aplicación cambiar la creación de 
objetos sin cambiar el código que los utiliza.
"""


class Shape:
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print("Dibujando un rectángulo.")

class Circle(Shape):
    def draw(self):
        print("Dibujando un círculo.")

class ShapeFactory:
    def get_shape(self, shape_type):
        if shape_type is None:
            return None
        if shape_type == "CIRCLE":
            return Circle()
        elif shape_type == "RECTANGLE":
            return Rectangle()
        return None

def main():
    shape_factory = ShapeFactory()
    shape1 = shape_factory.get_shape("CIRCLE")
    shape1.draw()
    shape2 = shape_factory.get_shape("RECTANGLE")
    shape2.draw()

if __name__ == "__main__":
    main()
