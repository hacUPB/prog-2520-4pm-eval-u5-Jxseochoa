lista = ["Do it again","Fiesta","Tu amor no tiene fin","Ya no soy esclavo","Tómalo"]
ruta = "C:\\Users\\Control\\Downloads"
file_name = "canciones.txt"
modo = "w"

for i in range(len(lista)):
    lista[i] = lista[i] + "\n"

print(lista)

fp = open(ruta + "\\" + file_name, modo, encoding="utf-8")
#fp.writelines(lista)
for cancion in lista:
    fp.write(cancion + "\n")
fp.close()
