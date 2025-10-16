#1. Abrir el archivo 
fp = open("C:\\Users\\B09S202est\\Desktop\\archivo1.docx", "r", encoding="utf-8")
#2. Leer el archivo
#datos = fp.read(20)
#datos = fp.read()
datos = fp.readline()
#3. Cerrar el archivo
fp.close()

print(datos)