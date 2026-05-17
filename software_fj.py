from abc import ABC, abstractmethod
import logging

# Configuración del archivo log
logging.basicConfig(
    filename="errores.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Excepción personalizada
class ErrorReserva(Exception):
    pass


# Clase abstracta Persona
class Persona(ABC):

    @abstractmethod
    def mostrar(self):
        pass


# Clase Cliente
class Cliente(Persona):

    def __init__(self, nombre, correo):

        if not nombre:
            raise ValueError("El nombre no puede estar vacío")

        if "@" not in correo:
            raise ValueError("Correo inválido")

        self.__nombre = nombre
        self.__correo = correo

    def mostrar(self):
        return f"Cliente: {self.__nombre}"

    @property
    def nombre(self):
        return self.__nombre


# Clase abstracta Servicio
class Servicio(ABC):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self, tiempo):
        pass


# Servicio Sala
class Sala(Servicio):

    def calcular_costo(self, horas):
        return self.precio * horas


# Servicio Equipo
class Equipo(Servicio):

    def calcular_costo(self, dias):
        return self.precio * dias


# Servicio Asesoria
class Asesoria(Servicio):

    def calcular_costo(self, horas):
        return self.precio * horas


# Clase Reserva
class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise ErrorReserva("Duración inválida")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):

        try:

            costo = self.servicio.calcular_costo(
                self.duracion
            )

            self.estado = "Confirmada"

            print(f"Reserva exitosa")
            print(f"Cliente: {self.cliente.nombre}")
            print(f"Servicio: {self.servicio.nombre}")
            print(f"Costo total: ${costo}")

        except Exception as e:

            logging.error(str(e))

            print("Error al confirmar la reserva")


# Lista de operaciones
operaciones = []


# OPERACIÓN 1
try:

    cliente1 = Cliente(
        "Juan",
        "juan@gmail.com"
    )

    servicio1 = Sala(
        "Sala VIP",
        50000
    )

    reserva1 = Reserva(
        cliente1,
        servicio1,
        2
    )

    operaciones.append(reserva1)

except Exception as e:

    logging.error(str(e))


# OPERACIÓN 2 (inválida)
try:

    cliente2 = Cliente(
        "",
        "correo"
    )

except Exception as e:

    logging.error(str(e))
    print("Error:", e)


# Ejecutar reservas
for op in operaciones:
    op.confirmar()
