import csv 
# Crear la lista de temperatura, humedad y presión y leer los datos del archivo
humedad = []
with open('C:\\Users\\Control\\Desktop\\Variables.csv', 'r') as archivo_csv:
    lector = csv.reader(archivo_csv, delimiter=';')
    encabezados = next(lector)
    for fila in lector:
        dato = fila[1]
        try:
            dato = float(dato.replace(',', '.'))
        except:
            print("Dato no encontrado")
            dato = 0.0
        humedad.append(dato)

    archivo_csv
