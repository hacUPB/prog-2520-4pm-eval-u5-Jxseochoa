import os
import csv
import math
import matplotlib.pyplot as plt

# MENÚ PRINCIPAL 

def mostrar_menu_principal():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Listar archivos")
    print("2. Procesar archivo de texto (.txt)")
    print("3. Procesar archivo CSV (.csv)")
    print("4. Salir")

def listar_archivos():
    print("Archivos en la carpeta actual:")
    try:
        elementos = os.listdir()
        i = 0
        while i < len(elementos):
            print("-", elementos[i])
            i += 1
    except:
        print("No fue posible listar los archivos")

# Txt

def contar_palabras_y_caracteres(nombre):
    try:
        f = open(nombre, "r", encoding="utf-8")
        texto = f.read()
        f.close()
    except:
        print("No se pudo leer el archivo")
        return

    palabras = texto.split()
    total_palabras = 0
    i = 0
    while i < len(palabras):
        total_palabras += 1
        i += 1

    caracteres_con = 0
    i = 0
    while i < len(texto):
        caracteres_con += 1
        i += 1

    caracteres_sin = 0
    i = 0
    while i < len(texto):
        if not texto[i].isspace():
            caracteres_sin += 1
        i += 1

    print("Total de palabras:", total_palabras)
    print("Caracteres (con espacios):", caracteres_con)
    print("Caracteres (sin espacios):", caracteres_sin)


def reemplazar_palabra(nombre):
    buscar = input("Palabra a buscar: ")
    nueva = input("Palabra para reemplazar: ")
    try:
        f = open(nombre, "r", encoding="utf-8")
        texto = f.read()
        f.close()
    except:
        print("No se pudo leer el archivo")
        return

    texto_nuevo = texto.replace(buscar, nueva)

    try:
        f = open(nombre, "w", encoding="utf-8")
        f.write(texto_nuevo)
        f.close()
        print("Reemplazo realizado")
    except:
        print("No se pudo escribir el archivo")

def histograma_vocales(nombre):
    try:
        f = open(nombre, "r", encoding="utf-8")
        texto = f.read()
        f.close()
    except:
        print("No se pudo leer el archivo")
        return

    vocales = ["a", "e", "i", "o", "u"]
    conteo = [0, 0, 0, 0, 0]

    i = 0
    while i < len(texto):
        letra = texto[i]
        j = 0
        while j < len(vocales):
            if letra == vocales[j]:
                conteo[j] += 1
                break
            j += 1
        i += 1

    i = 0
    while i < len(vocales):
        print(vocales[i], ":", conteo[i])
        i += 1

    try:
        posiciones = []
        i = 0
        while i < len(vocales):
            posiciones.append(i)
            i += 1
        plt.figure()
        plt.bar(posiciones, conteo)
        plt.xticks(posiciones, vocales)
        plt.title("Histograma de vocales")
        plt.xlabel("Vocal")
        plt.ylabel("Frecuencia")
        plt.tight_layout()
        plt.show()
    except:
        print("No se pudo graficar")


def menu_txt():
    nombre = input("Nombre del archivo .txt: ")
    if not os.path.exists(nombre):
        print("No existe ese archivo")
        return

    while True:
        print("=== SUBMENÚ TXT ===")
        print("1. Contar palabras y caracteres")
        print("2. Reemplazar palabra")
        print("3. Histograma de vocales")
        print("4. Volver")
        op = input("Opción: ")

        if op == "1":
            contar_palabras_y_caracteres(nombre)
        elif op == "2":
            reemplazar_palabra(nombre)
        elif op == "3":
            histograma_vocales(nombre)
        elif op == "4":
            break
        else:
            print("Opción no válida")

# CSV

def leer_csv(nombre):
    datos = []
    try:
        f = open(nombre, "r", encoding="utf-8")
        lector = csv.reader(f)
        for fila in lector:
            datos.append(fila)
        f.close()
    except:
        print("No se pudo leer el CSV")
    return datos

def mostrar_15_filas(datos):
    print("Primeras 15 filas:")
    limite = 15
    i = 0
    while i < len(datos) and i < limite:
        print(datos[i])
        i += 1

def lista_a_float_columna(datos, col):
    valores = []
    i = 1  
    while i < len(datos):
        fila = datos[i]
        if col < len(fila):
            try:
                v = float(fila[col])
                valores.append(v)
            except:
                pass
        i += 1
    return valores

def burbuja_ordenar(lista_nums):
    n = len(lista_nums)
    k = 0
    while k < n - 1:
        j = 0
        while j < n - 1 - k:
            if lista_nums[j] > lista_nums[j + 1]:
                tmp = lista_nums[j]
                lista_nums[j] = lista_nums[j + 1]
                lista_nums[j + 1] = tmp
            j += 1
        k += 1

def estadisticas_basicas(valores):
    n = 0
    i = 0
    while i < len(valores):
        n += 1
        i += 1

    if n == 0:
        return n, 0.0, 0.0, 0.0, 0.0

    suma = 0.0
    i = 0
    while i < n:
        suma += valores[i]
        i += 1
    promedio = suma / n

    minimo = valores[0]
    maximo = valores[0]
    i = 1
    while i < n:
        if valores[i] < minimo:
            minimo = valores[i]
        if valores[i] > maximo:
            maximo = valores[i]
        i += 1

    copia = []
    i = 0
    while i < n:
        copia.append(valores[i])
        i += 1
    burbuja_ordenar(copia)
    if n % 2 == 1:
        mediana = copia[n // 2]
    else:
        mediana = (copia[n // 2 - 1] + copia[n // 2]) / 2.0

    suma_dif = 0.0
    i = 0
    while i < n:
        d = copia[i] - promedio
        suma_dif += d * d
        i += 1
    desv = math.sqrt(suma_dif / n)

    return n, promedio, mediana, desv, minimo, maximo

def calcular_estadisticas(datos):
    if len(datos) == 0:
        print("CSV vacío")
        return
    encabezado = datos[0]
    print("Columnas disponibles:")
    i = 0
    while i < len(encabezado):
        print(i, ":", encabezado[i])
        i += 1

    try:
        col = int(input("Número de columna: "))
    except:
        print("Índice inválido")
        return

    valores = lista_a_float_columna(datos, col)
    if len(valores) == 0:
        print("La columna no tiene datos numéricos")
        return

    res = estadisticas_basicas(valores)
    print("n:", res[0])
    print("Promedio:", res[1])
    print("Mediana:", res[2])
    print("Desv. estándar:", res[3])
    print("Mínimo:", res[4])
    print("Máximo:", res[5])

def grafico_dispersion(valores, titulo, etiqueta_y):
    x = []
    i = 0
    while i < len(valores):
        x.append(i)
        i += 1
    plt.figure()
    plt.scatter(x, valores)
    plt.title(titulo)
    plt.xlabel("Índice")
    plt.ylabel(etiqueta_y)
    plt.tight_layout()
    plt.show()

def grafico_barras_categorias(datos, col):
    categorias = []
    conteos = []
    i = 1
    while i < len(datos):
        fila = datos[i]
        if col < len(fila):
            clave = fila[col]
        else:
            clave = ""

        pos = -1
        j = 0
        while j < len(categorias):
            if categorias[j] == clave:
                pos = j
                break
            j += 1

        if pos == -1:
            categorias.append(clave)
            conteos.append(1)
        else:
            conteos[pos] = conteos[pos] + 1
        i += 1

    if len(categorias) == 0:
        print("No hay categorías para graficar")
        return

    if len(categorias) > 30:
        print("Muchas categorías, se muestran solo 30")
        categorias = categorias[:30]
        conteos = conteos[:30]

    posiciones = []
    i = 0
    while i < len(categorias):
        posiciones.append(i)
        i += 1

    plt.figure()
    plt.bar(posiciones, conteos)
    plt.xticks(posiciones, categorias, rotation=90)
    plt.title("Frecuencia por categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()

def graficar_csv(datos):
    if len(datos) == 0:
        print("CSV vacío")
        return

    encabezado = datos[0]
    print("Columnas disponibles:")
    i = 0
    while i < len(encabezado):
        print(i, ":", encabezado[i])
        i += 1

    print("1. Gráfico de dispersión de una columna numérica")
    print("2. Gráfico de barras por frecuencia de una columna categórica")
    op = input("Opción: ")

    if op == "1":
        try:
            col = int(input("Número de columna numérica: "))
        except:
            print("Índice inválido")
            return
        valores = lista_a_float_columna(datos, col)
        if len(valores) == 0:
            print("La columna no tiene datos numéricos")
            return
        grafico_dispersion(valores, "Dispersión de " + encabezado[col], encabezado[col])

    elif op == "2":
        try:
            col = int(input("Número de columna categórica: "))
        except:
            print("Índice inválido")
            return
        grafico_barras_categorias(datos, col)

    else:
        print("Opción no válida")

def menu_csv():
    nombre = input("Nombre del archivo .csv: ")
    if not os.path.exists(nombre):
        print("No existe ese archivo")
        return

    datos = leer_csv(nombre)

    while True:
        print("SUBMENÚ CSV ")
        print("1. Mostrar las 15 primeras filas")
        print("2. Calcular estadísticas")
        print("3. Graficar datos")
        print("4. Volver")
        op = input("Opción: ")

        if op == "1":
            mostrar_15_filas(datos)
        elif op == "2":
            calcular_estadisticas(datos)
        elif op == "3":
            graficar_csv(datos)
        elif op == "4":
            break
        else:
            print("Opción no válida")

# INICIO

def main():
    while True:
        mostrar_menu_principal()
        op = input("Elige una opción: ")

        if op == "1":
            listar_archivos()
        elif op == "2":
            menu_txt()
        elif op == "3":
            menu_csv()
        elif op == "4":
            print("Hasta luego")
            break
        else:
            print("Opción no válida")

main()
