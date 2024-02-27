"""
Autor: Santiago Manco Maya
Contacto: Teams
Fecha: 26/02/2024
Descripción: El siguiente código tiene como objetivo resolver el ejercicio de implementación
del hospital dado a los estudiantes por el monitor de EDA1 Santiago Manco Maya para lograr
un mayor entendimiento acerca de apuntadores, unidad de dato, nodos, listas simplemente enlazadas,
pilas y colar; potenciando habilidades algoritmicas en la resolución de problemas reales.
Ejercicio opcional para los estudiantes: Implementen este mismo ejercicio usando listas doblemente
enlazadas o usando un apuntador para el último elemento de la lista simplemente enlazada.

Nota: Si tienen alguna duda sobre este algoritmo, se las resolveré en los espacios de monitoría
publicados.
"""


# Importación de librerias
import random  # Importamos random para poder tener datos aleatorios

# Importacion de clases
from lista import SingleLinkedList  # Importamos la clase SingleLinkedList de lista.py
from dato import Dato  # Importamos la clase Dato de dato.py

# Main
if __name__ == "__main__":

    lista = SingleLinkedList()  # Creamos nuestra lista simplemente enlazada llamada lista

    names = ["Santiago", "Carlos", "Edison", "Juan José", "Luciana", "Marta"]  # Nombres para escoger aleatoriamente
    lastnames = ["Manco", "Díaz", "Gómez", "Vélez", "Pérez", "Martinez", "Gutierrez"]  # Apellidos para escoger aleatoriamente

    print("-" * 50)  # Imprime una sucesión de 50 simbolos - para crear una separación (multiplicación)
    print("Bienvenid@ al sistema de cola de urgencias de un hospital")  # Mensaje de bienvenida
    print("-" * 50)
    print("Lista de pacientes que llegan al hospital:")
    print("-" * 50)

    for i in range(10):  # Con este ciclo, añadimos 10 personas a la fila del hospital (datos "Dummy")

        # Guardamos a una persona con nombre, apellido y edad aleatoria en newPerson
        newPerson = Dato(random.choice(names), random.choice(lastnames), random.randint(18, 70))

        # Condicional para saber si se encola o se le hace push al nodo según el estado del paciente
        if newPerson.estado == "Urgente":
            lista.push(newPerson)  # Si el estado es Urgente, se le coloca de primero en la fila usando el método push de lista
        else:
            lista.encolar(newPerson)  # Si no, el paciente, que tiene estado Leve, se coloca al final de la fila

    lista.printList() # Imprimimos la lista
    print("-" * 50)

    # Atendemos a los graves:


    # Iteramos mientras el nodo que vamos a sacar (la cabeza) no es nulo y su estado es urgente
    while lista.head is not None and lista.head.dato.estado == "Urgente":
        outNode = lista.pop()  # Guardamos el nodo que nos retorna el método pop en outNode (el nodo que se sacó)
        print(f'Se ha atendido al paciente urgente {outNode.dato.nom} {outNode.dato.apellido}')

    print("-" * 50)
    print("Los pacientes graves han sido antendidos y ahora quedan en la fila: ")
    print("-" * 50)
    lista.printList()  # Imprimimos la lista solo con los pacientes leves
    print("-" * 50)

    # Atendemos a los leves:

    # Iteramos mientras el nodo que vamos a sacar (la cabeza) no es nulo
    while lista.head is not None:
        outNode = lista.pop()  # Guardamos el nodo que nos retorna el método pop en outNode (el nodo que se sacó)
        print(f'Se ha atendido al paciente leve {outNode.dato.nom} {outNode.dato.apellido}')

    print("-" * 50)
    print("¡Se han atendido a todos los pacientes!")
    print("-" * 50)
