from abc import ABC, abstractmethod
import logging

# Configurar archivo de errores
logging.basicConfig(
    filename="errores.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Excepción personalizada
class ErrorReserva(Exception):
    pass


# Clase abstracta
class Persona(ABC):

    @abstractmethod
    def mostrar(self):
        pass


# Cliente
class Cliente(Persona):

    def __init__(self, nombre, correo):

        if nombre.strip() == "":
            raise ValueError("Nombre vacío")

        if "@" not in correo:
            raise ValueError("Correo inválido")

        self.__nombre = nombre
        self.__correo = correo

    @property
    def nombre(self):
        return self.__nombre

    def mostrar(self):
        return f"Cliente: {self.__nombre}"


# Clase abstracta Servicio
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


class Equipo(Servicio):

    def calcular_costo(self, tiempo):
        return self.precio * tiempo


class Asesoria(Servicio):

    def calcular_costo(self, tiempo):
        return self.precio * tiempo


# Reserva
class Reserva:

    def __init__(self, cliente, servicio, tiempo):

        if tiempo <= 0:
            raise ErrorReserva(
                "Tiempo inválido"
            )

        self.cliente = cliente
        self.servicio = servicio
        self.tiempo = tiempo
        self.estado = "Pendiente"

    def confirmar(self):

        try:

            costo = self.servicio.calcular_costo(
                self.tiempo
            )

            self.estado = "Confirmada"

            print("\nReserva exitosa")
            print("Cliente:", self.cliente.nombre)
            print("Servicio:", self.servicio.nombre)
            print("Costo:", costo)

        except Exception as e:

            logging.error(str(e))
            print("Error:", e)


reservas = []


# Operación válida 1
try:
    c1 = Cliente(
        "Juan",
        "juan@gmail.com"
    )

    s1 = Sala(
        "Sala VIP",
        50000
    )

    r1 = Reserva(
        c1,
        s1,
        2
    )

    reservas.append(r1)

except Exception as e:
    logging.error(str(e))


# Operación válida 2
try:
    c2 = Cliente(
        "Ana",
        "ana@gmail.com"
    )

    s2 = Equipo(
        "Proyector",
        30000
    )

    r2 = Reserva(
        c2,
        s2,
        3
    )

    reservas.append(r2)

except Exception as e:
    logging.error(str(e))


# Operación inválida
try:

    c3 = Cliente(
        "",
        "correo"
    )

except Exception as e:

    logging.error(str(e))
    print("\nError detectado:", e)


for r in reservas:
    r.confirmar()
