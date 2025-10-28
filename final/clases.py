from datetime import datetime

# Creación de clases Cliente, Evento y Venta
class Cliente:
    def __init__(self, id_cliente: int, nombre: str, email: str, fecha_alta: datetime):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.fecha_alta = fecha_alta
    
    def __str__(self) -> str:
        return f"[Cliente ID: {self.id_cliente} - Cliente: {self.nombre} - Email: {self.email} - Alta: {self.fecha_alta}]"

    def antiguedad_dias(self) -> int:
        hoy = datetime.today().date()
        return (hoy - self.fecha_alta).days
        
class Evento:
    def __init__(self, id_evento: int, nombre: str, categoria: str, fecha_evento: datetime, precio: float):
        self.id_evento = id_evento
        self.nombre = nombre
        self.categoria = categoria
        self.fecha_evento = fecha_evento
        self.precio = precio
    
    def __str__(self) -> str:
        return f"[Evento ID: {self.id_evento} - Evento: {self.nombre} - Categoría: {self.categoria} - Fecha: {self.fecha_evento} - Precio: {self.precio}€]"

    def dias_hasta_evento(self) -> int:
        hoy = datetime.today().date()
        return (self.fecha_evento - hoy).days
        
class Venta:
    def __init__(self, id_venta: int, id_cliente: int, id_evento: int, fecha_venta: datetime, total: float):
        self.id_venta = id_venta
        self.id_cliente = id_cliente
        self.id_evento = id_evento
        self.fecha_venta = fecha_venta
        self.total = total
    
    def __str__(self) -> str:
        return f"[Venta: ID {self.id_venta} - Cliente ID: {self.id_cliente} - Evento ID: {self.id_evento} - Fecha: {self.fecha_venta} - Total: {self.total}€]"
