import csv
from datetime import datetime
from clases import Cliente, Evento, Venta
from funciones import clientes, eventos, ventas, guardar_cliente, cargar_estadisticas


# Menu
def menu():
    while True:
        print('CRM de eventos')
        print('1. Listar clientes, eventos o ventas')
        print('2. Dar de alta un cliente')
        print('3. Filtrar ventas por rango de fechas')
        print('4. Mostrar estadísticas')
        print('5. Exportar informe resumen a CSV')
        print('0. Salir')
        
        try:
            respuesta = int(input('Elige una opción: '))
            print()
        except ValueError: 
            print('Error: La respuesta debe ser un número entero. Inténtelo de nuevo.')
            continue
        
        match(respuesta):
            case 0:
                break
            case 1:
                listar_tipo_dato()
            case 2:
                alta_cliente()  
            case 3:
                filtrar_ventas_por_rango() 
            case 4:
                mostrar_estadisticas() 
            case 5:
                exportar_informe()  
            case _:
                print("Opción no válida. Inténtelo de nuevo.")
                
        print()

# Método del menú para listar un tipo de dato (clientes, eventos, ventas). 
def listar_tipo_dato():
    # Submenu para que escoja el tipo de dato
    while True:
        print('Escoge lista de datos') 
        print("1. Clientes")
        print("2. Eventos")
        print("3. Ventas")
        print("0.Salir")
        
        try:
            respuesta = int(input('Elige una opción: '))
            print()
        except ValueError: 
            print('La respuesta debe ser un número entero. Inténtelo de nuevo.')
            continue
        
        # Se imprimer bien porque cada clase tiene __str__
        match(respuesta):
            case 0:
                break
            case 1: 
                for cliente in clientes.values():
                    print(cliente)
                break
            case 2:
                for evento in eventos.values():
                    print(evento)
                break 
            case 3:
                for venta in ventas.values():
                    print(venta)
                break 
            case _:
                print("Opción no válida. Inténtelo de nuevo.")
                
        print()

# Método del menú para dar de alta a un cliente. 
def alta_cliente():
    # Registro para poner las credenciales nombre y email. No pueden estar vacios.
    while True:
        print('Registro de cliente')
        nombre = input('Introduce el nombre: ')
        if not nombre:
            print('El nombre está vacío. Inténtelo de nuevo.')
            continue
        
        # Se valida el email para que tenga "@" y "." obligatoriamente
        email = input('Introduce email: ')
        if not email or not "@" in email or not "." in email:
            print('El email no es válido. Inténtelo de nuevo.')
            continue
            
        break
    
    # Buscar el primer ID libre del mapa de clientes
    nuevo_id = 1
    while nuevo_id in clientes:
        nuevo_id += 1
    
    # Agregar el nuevo cliente 
    cliente = Cliente(nuevo_id, nombre, email, datetime.now().date())
    clientes[int(nuevo_id)] = cliente
    
    # Guardar en csv
    guardar_cliente(cliente)
    
    print(f'Nuevo cliente registrado: {cliente}')

# Método del menú para ver las que ventas que hay entre un rango de fechas. 
def filtrar_ventas_por_rango():
    print('Filtrado de ventas segun un rango de fechas')
    while True:
        fecha_inicial_string = input('Introduce fecha inicial (YYYY-MM-DD): ')
        fecha_final_string = input('Introduce fecha final (YYYY-MM-DD): ')
        
        # Para comprobar que es una fecha, si strtime ve que la fecha no es (YYYY-MM-DD), da error
        try:
            fecha_inicial = datetime.strptime(fecha_inicial_string, "%Y-%m-%d").date()
        except:
            print('Las fechas de inicial no tiene el formato correcto. Inténtelo de nuevo')
            continue
        
        try:
            fecha_final = datetime.strptime(fecha_final_string, "%Y-%m-%d").date()
        except:
            print('Las fecha final no tiene el formato correcto. Inténtelo de nuevo')
            continue
        
        break

    print()
    print(f'Ventas del {fecha_inicial} al {fecha_final}:')
    hay_ventas = False
    for venta in ventas.values():
        if fecha_inicial <= venta.fecha_venta <= fecha_final:
            hay_ventas = True
            print(venta)
    if not hay_ventas:
        print('No hay ventas.')        
    


# Método del menú para mostrar estadísticas como ingresos totales, ingresos por evento...
def mostrar_estadisticas():
    ingresos_totales, ingresos_por_evento, categorias_existentes, dias_proximo_evento, tupla_precios = cargar_estadisticas()
    
    print('Estadísticas\n')
        
    print(f'Ingresos totales: {ingresos_totales}\n')
        
    print('Ingresos por evento:')
    for i in ingresos_por_evento:
        print(i)
    print()
    
    print(f'Categorias existentes:')
    for i in categorias_existentes:
        print(i)
    print()
    
    if dias_proximo_evento is None:
        print("No hay eventos próximos.")
    else:
        print(f"Días hasta el evento más próximo: {dias_proximo_evento}\n")
        
    print('Precios:')
    print(f'mínimo: {tupla_precios[0]:.2f}')
    print(f'máximo: {tupla_precios[1]:.2f}')
    print(f'media: {tupla_precios[2]:.2f}')

# Método para crear informe.csv a la carpeta data
def exportar_informe():
    ingresos_totales, ingresos_por_evento, categorias_existentes, dias_proximo_evento, tupla_precios = cargar_estadisticas()
    
    try:
        with open('data/informe.csv', 'w', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo, delimiter=';', quotechar='"')

            writer.writerow(['Informe de estadísticas'])
            writer.writerow([])
            writer.writerow(['Ingresos totales', ingresos_totales])
            writer.writerow([])

            writer.writerow(['Ingresos por evento'])
            writer.writerow(['Evento', 'Ingresos'])
            for evento, total in ingresos_por_evento.items():
                writer.writerow([evento, total])
            writer.writerow([])

            writer.writerow(['Categorías existentes'])
            for categoria in categorias_existentes:
                writer.writerow([categoria])
            writer.writerow([])

            if dias_proximo_evento is not None:
                writer.writerow(['Días hasta el próximo evento', dias_proximo_evento])
            else:
                writer.writerow(['No hay eventos próximos'])
            writer.writerow([])

            if tupla_precios:
                writer.writerow(['Precios de eventos'])
                writer.writerow(['Mínimo', 'Máximo', 'Media'])
                writer.writerow([f'{tupla_precios[0]:.2f}', f'{tupla_precios[1]:.2f}', f'{tupla_precios[2]:.2f}'])

        print('Informe exportado correctamente a data/informe.csv.')
    except:
        print('Error creando o sobrescribiendo el archivo clientes.csv.')
        exit()

    