# CRM de Eventos — Proyecto Final

## Descripción
Este programa es un pequeño CRM de gestión de eventos y ventas, que administrar clientes, eventos y ventas desde consola, y almacena datos en ficheros CSV.

Hace funcionalidades como listar datos, dar de alta clientes, filtrar ventas por rango de fechas, mostrar estadísticas y exportar informes.

---

## Estructura del proyecto

* `project/`
    * `data/`
        * `clientes.csv`
        * `eventos.csv`
        * `ventas.csv`
        * `informe.csv` (se genera automáticamente)
    * `clases.py`
    * `funciones.py`
    * `menu.py`
    * `main.py`

---

## Funcionalidades principales

### 1. Cargar datos
- Se ejecuta automáticamente al iniciar el programa.
- Lee los archivos CSV (`clientes.csv`, `eventos.csv`, `ventas.csv`) y los guarda en diccionarios.
- Si un archivo no existe, muestra un mensaje de error.

### 2. Listar datos
- Permite listar clientes, eventos o ventas. El usuario elige.
- Cada clase tiene su método `__str__()` para mostrar la información formateada.

### 3. Alta de cliente
- Pide nombre y email por consola.
- Valida que no estén vacíos y que el email contenga “@” y “.”.
- Asigna un ID automático, buscando el primer libre.
- Guarda el cliente en el diccionario y lo añade al final del CSV (`clientes.csv`).

### 4. Filtrar ventas por rango de fechas
- Pide las 2 fechas en formato `YYYY-MM-DD`.
- Muestra las ventas comprendidas entre las dos fechas.
- Valida el formato con `datetime.strptime`.

### 5. Mostrar estadísticas
Muestra por consola:
- Ingresos totales.
- Ingresos por evento.
- Categorías existentes.
- Días hasta el evento más próximo.
- Precio mínimo, máximo y medio de los eventos.

### 6. Exportar informe
- Genera un archivo `data/informe.csv` con las estadísticas anteriores.

---

## Clases 

### Cliente
- Atributos: `id_cliente`, `nombre`, `email`, `fecha_alta`.
- Métodos:
  - `__str__()` → muestra los datos formateados.
  - `antiguedad_dias()` → devuelve los días desde la fecha de alta.

### Evento
- Atributos: `id_evento`, `nombre`, `categoria`, `fecha_evento`, `precio`.
- Métodos:
  - `__str__()` → muestra los datos formateados.
  - `dias_hasta_evento()` → devuelve los días que faltan para el evento.

### Venta
- Atributos: `id_venta`, `id_cliente`, `id_evento`, `fecha_venta`, `total`.
- Métodos:
  - `__str__()` → muestra los datos formateados.

---

## Ejecución
Ejecutar el programa desde la carpeta principal:

```bash
python main.py

