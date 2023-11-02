# Patrones de diseño en Python
Este repositorio contiene ejemplos de implementación de los patrones de diseño 
Singleton, Builder y Factory en Python. Cada patrón está documentado en un 
archivo individual con un ejemplo de código funcional.

## Singleton
El patrón de diseño Singleton asegura que una clase tenga solo una instancia y 
proporciona un punto de acceso global a ella. Esto es útil cuando se necesita 
tener una única instancia compartida de una clase en toda la aplicación.

## Builder
El patrón de diseño Builder separa la construcción de un objeto complejo de su 
representación, de tal manera que el mismo proceso de construcción puede crear 
diferentes representaciones. Esto es útil cuando se necesita construir objetos 
complejos con diferentes partes o configuraciones.

## Factory
El patrón de diseño Factory es una técnica de creación de objetos que delega la 
creación de objetos a una clase fábrica en lugar de crear objetos directamente 
en el código cliente. Esto es útil cuando se necesita crear diferentes objetos 
basados en algunos datos de entrada o lógica de negocios.


## MVC
El patrón MVC es especialmente conveniente en situaciones donde se necesita una 
separación clara entre la lógica de negocio, la presentación de datos y la 
interacción del usuario. Aquí hay algunas situaciones en las que puede ser 
beneficioso aplicar el patrón 


## DECORADOR
El Patrón Decorator es un patrón de diseño estructural que permite agregar 
funcionalidades adicionales a un objeto existente sin alterar su estructura 
básica. Se logra envolviendo el objeto original con uno o más decoradores, 
que son clases que implementan la misma interfaz que el objeto que están 
decorando. Los decoradores pueden anidar para proporcionar una serie de 
funcionalidades en capas.

Componente: Este es la interfaz común que tanto los componentes concretos como 
los decoradores deben implementar. Define las operaciones que los decoradores 
y los componentes concretos comparten.

Componente Concreto: Estas son las clases que implementan la interfaz del 
componente. Representan la funcionalidad base a la que se pueden agregar decoradores.

Decorador: Esta es la clase abstracta que extiende la interfaz del componente y
contiene una referencia a un componente concreto. Los decoradores agregan 
funcionalidad adicional antes o después de delegar la llamada al componente concreto.

## Método de Plantilla
El patrón de diseño Método de Plantilla (Template Method) es un patrón de diseño 
de comportamiento que define la estructura básica de un algoritmo en una 
superclase, pero delega algunos pasos específicos de ese algoritmo a las 
subclases. De esta manera, permite que las subclases redefinan ciertos pasos 
del algoritmo sin cambiar su estructura general.

# Componentes del Patrón:

Clase Abstracta (Abstract Class): Esta es la clase base que define la estructura 
del algoritmo en términos de métodos abstractos (métodos que se declaran pero 
no se implementan en la clase base). Los métodos concretos en la clase 
abstracta son los pasos del algoritmo que no deben cambiar.

Método Plantilla (Template Method): Este es el método principal en la clase 
abstracta que define la secuencia de llamadas a los métodos abstractos y 
concretos que componen el algoritmo. Los pasos del algoritmo se definen en 
este método y no deben modificarse en las subclases.

Métodos Abstractos (Abstract Methods): Estos son los métodos declarados en la 
clase abstracta que representan los pasos del algoritmo que deben implementarse 
en las subclases.

Métodos Concretos (Concrete Methods): Estos son los métodos en la clase 
abstracta que proporcionan implementaciones predeterminadas para ciertos 
pasos del algoritmo. Estos métodos son opcionales y pueden ser sobrescritos 
por las subclases si es necesario.

Ventajas del Patrón de Diseño del Método de Plantilla:

Reutilización de Código: Permite la reutilización de la estructura de 
algoritmos sin duplicación de código.

Extensibilidad: Facilita la extensión de la funcionalidad del algoritmo 
mediante la creación de nuevas subclases que redefinen pasos específicos.

Mantenimiento: Cambiar o mejorar el algoritmo general es más fácil, ya que 
los cambios se realizan en un solo lugar, en la clase base.

## Instrucciones de uso
Para utilizar estos ejemplos, simplemente clone este repositorio y abra los 
archivos individuales para ver cada ejemplo de patrón de diseño. Asegúrese de 
tener una versión actual de Python instalada en su sistema.
