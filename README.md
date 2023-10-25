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

## Instrucciones de uso
Para utilizar estos ejemplos, simplemente clone este repositorio y abra los 
archivos individuales para ver cada ejemplo de patrón de diseño. Asegúrese de 
tener una versión actual de Python instalada en su sistema.
