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


registros = []
try:
    with open('horarios.csv', newline='', encoding='utf-8') as horarios_file:
        lector = csv.reader(horarios_file, delimiter=';', quotechar='"')
        
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


with open('madrugadores.csv', 'w', newline='') as madrugadores_file:
    writer = csv.writer(madrugadores_file, delimiter=';', quotechar='"')

def mostrar_registros():
    for registro in enumerate(registros.items(), start=1):
        print(registro)

def menu():
    while (True):
            print("\nPR03")
            print('1. Mostrar registros')
            print('2. Mostrar empleados por día')
            print('3. Generar reporte semanal')
            print('4. Generar reporte madrugadores')
            print('5. Consultar empleados Lunes y Viernes')
            print('6. Consultar empleados solo Sábado')
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
                    generar_reporte_semanal() 
                case 4:
                    generar_reporte_madrugadores() 
                case 5:
                    consultar_entre_semana() 
                case 6:
                    consultar_exclusivos_sabado() 
                case 7:
                    consultar_turnos_()
                case _:
                    print("Opción no válida. Inténtelo de nuevo.")

if __name__ == '__main__':
    menu()
