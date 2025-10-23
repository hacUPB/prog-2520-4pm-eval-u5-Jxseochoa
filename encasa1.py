# Solicitamos al usuario el nombre del archivo a crear
nombre_archivo = input("Ingrese el nombre del archivo de texto: ")

# Usamos 'with' para crear el contexto y escribir datos en el archivo 
with open(nombre_archivo, 'w') as archivo:
    print("Ingrese los datos que desea escribir en el archivo.")
    print("Agregue su información como jugador de baloncesto\n")

    # Solicitamos distintos tipos de datos
    texto = input("Información personal: ")
    numero = input("Número de años jugando: ")
    lista = input("Jugadores favoritos: ")

    # Escribimos todo en el archivo
    archivo.write("DATOS INGRESADOS\n")
    archivo.write(f"Información personal: {texto}\n")
    archivo.write(f"Número de años jugando: {numero}\n")
    archivo.write(f"Jugadores favoritos: {lista}\n")

# Ahora usamos 'with' para crear el contexto donde leer los datos del archivo
with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()
    print("\nContenido del archivo:")
    print(contenido)
