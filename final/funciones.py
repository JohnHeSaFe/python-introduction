import csv
from datetime import datetime
from clases import Cliente, Evento, Venta

clientes = {}
eventos = {}
ventas = {}
# Para que al principio del programa se carguen los datos.
def cargar_datos():
    # Mapas clientes, eventos y ventas, obtenidos desde los archivos csv con open() y csv.reader()
    # Cada elemento de los mapas es un objeto de la clase correspondiente
    
    try:
        with open('data/clientes.csv', newline='', encoding='utf-8') as clientes_file:
            lector = csv.reader(clientes_file, delimiter=';', quotechar='"')
            next(lector)
            
            for fila in lector:
                id_cliente, nombre, email, fecha_alta = fila
                clientes[int(id_cliente)] = Cliente(int(id_cliente), nombre, email, datetime.strptime(fecha_alta, "%Y-%m-%d").date())
    except FileNotFoundError:
        print('El archivo clientes.csv no se encontró. Ejecuta el programa desde la carpeta final.')
        exit()
    except:
        print('Error leyendo el archivo clientes.csv.')
        exit()

    try:
        with open('data/eventos.csv', newline='', encoding='utf-8') as eventos_file:
            lector = csv.reader(eventos_file, delimiter=';', quotechar='"')
            next(lector)
            for fila in lector:
                id_evento, nombre, categoria, fecha_evento, precio = fila
                eventos[int(id_evento)] = Evento(int(id_evento), nombre, categoria, datetime.strptime(fecha_evento, "%Y-%m-%d").date(), float(precio))
    except FileNotFoundError:
        print('El archivo eventos.csv no se encontró. Ejecuta el programa desde la carpeta final.')
        exit()
    except:
        print('Error leyendo el archivo eventos.csv')
        exit()

    try:
        with open('data/ventas.csv', newline='', encoding='utf-8') as ventas_file:
            lector = csv.reader(ventas_file, delimiter=';', quotechar='"')
            next(lector)
            for fila in lector:
                id_venta, id_cliente, id_evento, fecha_venta, total = fila
                ventas[int(id_venta)] = Venta(int(id_venta), int(id_cliente), int(id_evento), datetime.strptime(fecha_venta, "%Y-%m-%d").date(), float(total))
    except FileNotFoundError:
        print('El archivo ventas.csv no se encontró. Ejecuta el programa desde la carpeta final.')
        exit()
    except:
        print('Error leyendo el archivo ventas.csv.')
        exit()

# Para guardar el cliente en el csv despues de registrarle por alta_cliente()
def guardar_cliente(cliente: Cliente):
    try:
        with open('data/clientes.csv', 'a', newline='', encoding='utf-8') as clientes_file:
            writer = csv.writer(clientes_file, delimiter=';', quotechar='"')
            
            writer.writerow([cliente.id_cliente, cliente.nombre, cliente.email, cliente.fecha_alta.strftime("%Y-%m-%d")])
    except FileNotFoundError:
        print('El archivo clientes.csv no se encontró. Ejecuta el programa desde la carpeta final.')
        exit()
    except:
        print('Error escribiendo el archivo clientes.csv.')
        exit()

# Para cargar datos varios que se usaran en los métodos del menú mostrar_estadisticas() y exportar_informe()
# Devuelve 5 variables
def cargar_estadisticas():
    ingresos_totales = 0
    ingresos_por_evento = {}
    categorias_existentes = set()
    dias_proximo_evento = None
    tupla_precios = None
    
    for venta in ventas.values():
        ingresos_totales += venta.total
    
    # Primero se consiguen los eventos, y despues, por las ventas, se suman los ingresos segun el nombre del evento 
    for evento in eventos.values():
        ingresos_por_evento[evento.nombre] = 0
    for venta in ventas.values():
        evento = eventos[venta.id_evento]
        ingresos_por_evento[evento.nombre] += venta.total
    
    for evento in eventos.values():
        categorias_existentes.add(evento.categoria)
    
    # Para conseguir la fecha del proximo evento, se mira que sea mas futuro que hoy, y despues compara que sea el más cercano hasta el momento
    # Si no hay proximos conciertos, se queda None
    for evento in eventos.values():
        if evento.dias_hasta_evento() > 0 and (dias_proximo_evento is None or evento.dias_hasta_evento() < dias_proximo_evento):
            dias_proximo_evento = evento.dias_hasta_evento()
    
    precios = []
    for evento in eventos.values():
        precios.append(evento.precio)
    
    if precios:
        tupla_precios = [min(precios), max(precios), sum(precios)/len(precios)]
    
    return ingresos_totales, ingresos_por_evento, categorias_existentes, dias_proximo_evento, tupla_precios

    

    