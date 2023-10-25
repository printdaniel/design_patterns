# Componente (interfaz)
class InformeFinanciero:
    def obtener_informe(self):
        pass

# Componente Concreto
class InformeFinancieroBasico(InformeFinanciero):
    def obtener_informe(self):
        return "Informe financiero básico"

# Decorador Concreto
class DecoradorFormato(InformeFinanciero):
    def __init__(self, informe):
        self._informe = informe

    def obtener_informe(self):
        return self._informe.obtener_informe()

# Decorador de Encabezado
class DecoradorEncabezado(DecoradorFormato):
    def obtener_informe(self):
        return "Encabezado - " + super().obtener_informe()

# Decorador de Pie de Página
class DecoradorPiePagina(DecoradorFormato):
    def obtener_informe(self):
        return super().obtener_informe() + " - Pie de página"

# Uso
informe = InformeFinancieroBasico()
print("Informe básico:", informe.obtener_informe())

informe_con_encabezado = DecoradorEncabezado(informe)
print("Informe con encabezado:", informe_con_encabezado.obtener_informe())

informe_con_formato_completo = DecoradorPiePagina(informe_con_encabezado)
print("Informe con encabezado y pie de página:", informe_con_formato_completo.obtener_informe())
