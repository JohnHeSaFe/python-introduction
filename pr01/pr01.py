# Pedir el número de empleados. Tiene que ser un número positivo
while True:
    try:
        num_empleados = int(input("Introduce el número de empleados: "))
    except:
        print("Error, no se introdujo un número entero. Inténtalo de nuevo")
        continue

    if not num_empleados > 0: 
        print('Número de empleados debe ser positivo. Inténtalo de nuevo')

    break
        
# Pedir una hora de referencia. TIene que ser un número de 0 a 23
while True:
    try:
        hora_referencia = int(input("Introduce la hora de referencia inicial (0-23): "))
    except:
        print("Error, no se introdujo un número entero. Inténtalo de nuevo")
        continue
    
    if not 0 <= hora_referencia <= 23:
        print('Hora de referencia inicial debe ser entre 0 y 23. Inténtalo de nuevo')
        continue

    break
        

empleado_salida_temprana = ""
salida_mas_temprana = hora_referencia
contador_salidas = 0
# Pedir nombre, hora de entrada y salida de tantos empleados como num_empleados
for i in range(num_empleados):
    empleado_actual = input(f'Introduce nombre del empleado {i + 1}/{num_empleados}: ')
    while True:
        # Comprueba tambien cada hora
        try:
            hora_entrada = int(input("Introduce la hora de entrada del empleado " + empleado_actual + " (0-23): "))
            hora_salida = int(input("Introduce la hora de salida del empleado " + empleado_actual + " (0-23): "))
        except:
            print("Error, no se introdujo un número entero. Inténtalo de nuevo")
            continue
        
        if not 0 <= hora_entrada <= 23 or not 0 <= hora_salida <= 23:
            print('Hora de entrada y salida deben ser entre 0 y 23. Inténtalo de nuevo')
            continue

        # Tambien que la hora de entrada sea menor que la hora de salida
        if hora_entrada >= hora_salida:
            print('Hora de salida debe ser mayor a la hora de salida. Inténtalo de nuevo.')
            continue

        # Si está todo bien, si el empleado tiene la salida más temprana se le guarda el nombre y su hora de salida
        if hora_salida < salida_mas_temprana:
            salida_mas_temprana = hora_salida
            empleado_salida_temprana = empleado_actual
            contador_salidas += 1

        break

# Mustra el contador de salidas y el empleado que salió más antes
print(f'Número de empleados que salieron antes de la hora de referencia: {contador_salidas}')
print(f"Empleado con salida más temprana: {empleado_salida_temprana} ({salida_mas_temprana})")

        
            

