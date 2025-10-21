while True:
    try:
        num_empleados = int(input("Introduce el número de empleados: "))
    except:
        print("Error, no se introdujo un número entero. Inténtalo de nuevo")
        continue

    if not num_empleados > 0: 
        print('Número de empleados debe ser positivo. Inténtalo de nuevo')

    break
        

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
for i in range(num_empleados):
    empleado_actual = input(f'Introduce nombre del empleado {i + 1}/{num_empleados}: ')
    while True:
        try:
            hora_entrada = int(input("Introduce la hora de entrada del empleado " + empleado_actual + " (0-23): "))
            hora_salida = int(input("Introduce la hora de salida del empleado " + empleado_actual + " (0-23): "))
        except:
            print("Error, no se introdujo un número entero. Inténtalo de nuevo")
            continue
        
        if not 0 <= hora_entrada <= 23 or not 0 <= hora_salida <= 23:
            print('Hora de entrada y salida deben ser entre 0 y 23. Inténtalo de nuevo')
            continue

        if hora_entrada >= hora_salida:
            print('Hora de salida debe ser mayor a la hora de salida. Inténtalo de nuevo.')
            continue

        if hora_salida < salida_mas_temprana:
            salida_mas_temprana = hora_salida
            empleado_salida_temprana = empleado_actual
            contador_salidas += 1

        break

print(f'Número de empleados que salieron antes de la hora de referencia: {contador_salidas}')
print(f"Empleado con salida más temprana: {empleado_salida_temprana} ({salida_mas_temprana})")

        
            

