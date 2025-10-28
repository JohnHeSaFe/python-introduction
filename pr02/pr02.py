import json

# Dict global de todos los horarios recogidos del archivo horarios.json
# Si sale error sale del programa
try:
    with open('horarios.json', encoding='utf-8') as file:
        horarios = json.load(file)
except :
    print('Error leyendo el archivo horarios.json. Ejecuta el programa desde la carpeta pr02.')
    exit()

# Método del menú para mostrar todos los horarios de los empleados
def mostrar_registros():
    for horario in enumerate(horarios.items(), start=1):
        print(horario)

#Método del menú que, al pedir una hora de entrada (hh:mm), muestra cuantas personas entraron antes o a la hora entrada
def contar_entradas():
    contador = 0
    # Submenu para seguir pidiendo hasta que ponga una hora correcta
    while (True):
        hora_string = input('Introduce una hora de entrada: ')
        try:    
            hora = convertir_hora(hora_string)
        except ValueError as e:
            print(str(e) + " Inténtelo de nuevo")
            continue
    
        break
    
    for horario in horarios.items():
        hora_entrada = convertir_hora(horario[1][0])
        # hora[0] son las horas y hora[1] los minutos
        if (hora_entrada[0] < hora[0] or (hora_entrada[0] == hora[0] and hora_entrada[1] <= hora[1])):
            contador += 1

    print('Número de entradas: ' + str(contador))

# Se usa en contar_entradas() para que pueda convertir una hora en formato hh:mm a una lista numeros de dos elementos
def convertir_hora(hora_string):
    horario_entrada_dividida = hora_string.split(':')
        
    if len(horario_entrada_dividida) != 2:
        raise ValueError("El formato de la hora debe ser 'hh:mm'.")
    
    try:
        hora = int(horario_entrada_dividida[0])
        minuto = int(horario_entrada_dividida[1])
        return [hora, minuto]
    except:
        raise ValueError("Introduce números en formato 'hh:mm'.")

# Menu del programa para excoger las opciones
def menu():
    while (True):
        print("PR02")
        print('1. Mostrar registros')
        print('2. Contar entradas')
        print('0. Salir')
        
        try:
            respuesta = int(input('Elige opcion: '))
        except ValueError:
            print('La respuesta debe ser un número entero. Inténtelo de nuevo')
            continue
        
        match(respuesta):
            case 0:
                break
            case 1:
                mostrar_registros()
            case 2:
                contar_entradas()

if __name__ == '__main__':
    menu()
    file.close()
