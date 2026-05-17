from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    filename="errores.log",
    level=logging.ERROR,
    format="%(asctime)s - %(message)s"
)

class ErrorReserva(Exception):
    pass


class Persona(ABC):

    @abstractmethod
    def mostrar(self):
        pass


class Cliente(Persona):

    def __init__(self, nombre, correo):

        if nombre == "":
            raise ValueError("Nombre vacío")

        if "@" not in correo:
            raise ValueError("Correo inválido")

        self.__nombre = nombre
        self.__correo = correo

    @property
    def nombre(self):
        return self.__nombre

    def mostrar(self):
        return self.__nombre


class Servicio(ABC):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self, tiempo):
        pass


class Sala(Servicio):

    def calcular_costo(self, tiempo):
        return self.precio * tiempo


class Reserva:

    def __init__(self, cliente, servicio, tiempo):

        if tiempo <= 0:
            raise ErrorReserva("Tiempo inválido")

        self.cliente = cliente
        self.servicio = servicio
        self.tiempo = tiempo

    def confirmar(self):

        costo = self.servicio.calcular_costo(
            self.tiempo
        )

        print("Reserva exitosa")
        print("Cliente:", self.cliente.nombre)
        print("Servicio:", self.servicio.nombre)
        print("Costo:", costo)


cliente = Cliente(
    "Juan",
    "juan@gmail.com"
)

servicio = Sala(
    "Sala VIP",
    50000
)

reserva = Reserva(
    cliente,
    servicio,
    2
)

reserva.confirmar()
