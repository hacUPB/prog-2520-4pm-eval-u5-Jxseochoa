lista = ["Do it again","Fiesta","Tu amor no tiene fin","Ya no soy esclavo","Tómalo"]
ruta = "C:\\Users\\Control\\Downloads"
file_name = "canciones.txt"
file_info = ruta+"\\" + file_name
modo = "r"
with open(ruta + "\\" + file_name, modo, encoding="utf-8") as archivo:
    # hacer operaciones con el archivo
    for dato in archivo:
        print(dato)
