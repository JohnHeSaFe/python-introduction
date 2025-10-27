import csv
    
class RegistroHorario:
    def __init__(self, empleado: str, dia: str, entrada: int, salida: int):
        self.empleado = empleado
        self.dia = dia
        self.entrada = entrada
        self.salida = salida

    def duracion(self) -> int:
        """Devuelve la cantidad de horas trabajadas en este registro"""
        return self.salida - self.entrada
    
    def __str__(self) -> str:
        return f"[Empleado: {self.empleado} - Día: {self.dia} - Horario: {self.entrada:02d}:00 a {self.salida:02d}:00]"


registros = []
try:
    with open('horarios.csv', newline='', encoding='utf-8') as horarios_file:
        lector = csv.reader(horarios_file, delimiter=';', quotechar='"')
        next(lector)
        
        for fila in lector:
            # Cada fila es una lista de cadenas: [nombre, dia, entrada, salida]
            nombre, dia, h_entrada, h_salida = fila
            # Convertimos las horas a enteros
            entrada = int(h_entrada)
            salida = int(h_salida)
            registro = RegistroHorario(nombre, dia, entrada, salida)
            registros.append(registro)
except:
    print('Error leyendo el archivo horarios.csv. Ejecuta el programa desde la carpeta pr03.')
    exit()
    
empleados_por_dia = {}
for registro in registros:
    # Creamos el conjunto para el día si no existe
    if registro.dia not in empleados_por_dia:
        empleados_por_dia[registro.dia] = set()
    # Añadimos el empleado al conjunto del día
    empleados_por_dia[registro.dia].add(registro.empleado)

en_dos_dias = empleados_por_dia['Lunes'] & empleados_por_dia['Viernes']

sabado = empleados_por_dia.get('Sábado', set())
domingo = empleados_por_dia.get('Domingo', set())

exclusivos = sabado - domingo
    
# Calcular dias y horas totales por empleado
resumen = {}
for registro in registros:
    if registro.empleado not in resumen:
        resumen[registro.empleado] = {
            'dias': set(),
            'horas': 0
        }
    
    resumen[registro.empleado]['dias'].add(registro.dia)
    resumen[registro.empleado]['horas'] += registro.duracion()

def mostrar_registros():
    print('Registros de empleados:')
    for i, registro in enumerate(registros, start=1):
        print(f"{i}. {registro}")
        
def mostrar_empleados_por_dia():
    print('Empleados por día:')
    for dia, empleados in empleados_por_dia.items():
        print(f"{dia}: {empleados}")
    

def mostrar_empleados_lunes_viernes():
    print('Empleados que trabajaron lunes y viernes:')
    for empleado in en_dos_dias:
        print(empleado)
    
    with open('en_dos_dias.csv', 'w', newline='') as en_dos_dias_file:
        writer = csv.writer(en_dos_dias_file, delimiter=';')
        writer.writerow(['Nombre empleado'])
        for empleado in en_dos_dias:
            writer.writerow([empleado])
            
def consultar_exclusivos_sabado():
    print('Empleados que trabajaron el Sábado pero no el Domingo')
    for empleado in exclusivos:
        print(empleado)

    with open('exclusivos_sabado.csv', 'w', newline='', encoding='utf-8') as exclusivos_sabado_file:
        writer = csv.writer(exclusivos_sabado_file, delimiter=';')
        writer.writerow(['Empleado'])
        for empleado in exclusivos:
            writer.writerow([empleado])
    
def generar_reporte_semanal():
    # Escribir un resumen en un nuevo CSV
    with open('resumen_horarios.csv', 'w', newline='', encoding='utf-8') as resumen_horarios_file:
        escritor = csv.writer(resumen_horarios_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Cabecera
        escritor.writerow(['Empleado', 'Dias trabajados', 'Horas totales'])
        # Filas con los datos acumulados
        for empleado, datos in resumen.items():
            escritor.writerow([empleado, len(datos['dias']), datos['horas']])
    
    print("Se ha generado el fichero resumen_horarios.csv")
    
    
def generar_reporte_madrugadores():
    while True:
        try:
            hora_referencia = int(input('Introduce la hora de referencia (0-23): '))
            if 0 <= hora_referencia <= 23:
                break
            else:
                print('Hora de referencia debe ser entre 0 y 23. Inténtalo de nuevo')
        except:
            print("Error, no se introdujo un número entero. Inténtalo de nuevo")
    
    madrugadores = set()  
    for registro in registros:          
        if registro.entrada < hora_referencia: 
            madrugadores.add(registro.empleado)
        
    print('Empleados madrugadores')
    for e in madrugadores:
        print(e)
    
    with open('madrugadores.csv', 'w', newline='', encoding='utf-8') as madrugadores_file:
        writer = csv.writer(madrugadores_file, delimiter=';')
        writer.writerow(['Empleado'])
        for e in madrugadores:
            writer.writerow([e])
            
def consultar_turnos_largos():
    empleados_validos = set()
    empleados_descartados = set()

    for registro in registros:
        if registro.duracion() < 6:
            empleados_descartados.add(registro.empleado)
        else:
            if registro.empleado not in empleados_descartados:
                empleados_validos.add(registro.empleado)

    print("Empleados con todos los turnos de 6 horas o más:")
    for empleado in empleados_validos:
        print(empleado)
        
def menu():
    while (True):
            print("PR03")
            print('1. Mostrar registros')
            print('2. Mostrar empleados por día')
            print('3. Consultar empleados Lunes y Viernes')
            print('4. Consultar empleados Sábado pero no Domingo')
            print('5. Generar reporte semanal')
            print('6. Generar reporte madrugadores')
            print('7. Consultar empleados con todos los turnos de 6 o más horas')
            print('0. Salir')
        
            try:
                respuesta = int(input('Elige una opción: '))
            except ValueError: 
                print('Error: La respuesta debe ser un número entero. Inténtelo de nuevo.')
                continue
            
            match(respuesta):
                case 0:
                    break
                case 1:
                    mostrar_registros()
                case 2:
                    mostrar_empleados_por_dia()
                case 3:
                    mostrar_empleados_lunes_viernes()
                case 4:
                    consultar_exclusivos_sabado()
                case 5:
                    generar_reporte_semanal()
                case 6:
                    generar_reporte_madrugadores()
                case 7:
                    consultar_turnos_largos()
                case _:
                    print("Opción no válida. Inténtelo de nuevo.")
                    
            print()

if __name__ == '__main__':
    menu()
