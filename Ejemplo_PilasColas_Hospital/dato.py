# Importar librerias
import random  # Importamos la librería random que nos permitirá que el estado del paciente sea aleatorio


class Dato:  # Creamos la clase dato para guardar los datos del paciente

    # Método init para inicializar el constructor de la clase Nodo
    def __init__(self, nom, apellido, edad):  # Recibimos el nombre, apellido y edad del paciente
        self.nom = nom  # Guardamos el nombre del paciente en el atributo nom
        self.apellido = apellido  # Guardamos el apellido del paciente en el atributo apellido
        self.edad = edad  # Guardamos la edad del paciente en el atributo edad
        self.estado = random.choice(["Leve", "Urgente"])  # El método choice de random escoge aleatoriamente
                                                          # el estado del paciente

    # Método str que retorna los datos que se mostrarán cuando se imprima un objeto de la clase Dato
    def __str__(self):
        return f'Nombre: {self.nom}, Apellido: {self.apellido}, Edad: {self.edad}, Estado: {self.estado}'
