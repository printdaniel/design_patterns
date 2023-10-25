# Componente (interfaz)
class Cafe:
    def costo(self):
        pass

# Componente Concreto
class CafeSimple(Cafe):
    def costo(self):
        return 5

# Decorador Concreto
class LecheDecorator(Cafe):
    def __init__(self, cafe):
        self._cafe = cafe
    
    def costo(self):
        return self._cafe.costo() + 2

# Otro Decorador Concreto
class CanelaDecorator(Cafe):
    def __init__(self, cafe):
        self._cafe = cafe
    
    def costo(self):
        return self._cafe.costo() + 3

# Uso
cafe = CafeSimple()
print("Costo del café simple:", cafe.costo())

cafe_con_leche = LecheDecorator(cafe)
print("Costo del café con leche:", cafe_con_leche.costo())

cafe_con_canela = CanelaDecorator(cafe_con_leche)
print("Costo del café con leche y canela:", cafe_con_canela.costo())
