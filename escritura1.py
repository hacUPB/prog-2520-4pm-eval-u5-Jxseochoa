ruta = "C:\\Users\\Control\\Downloads" 
file_name="aviones.txt" 
modo = "w" 
fp = open(ruta+"\\"+file_name, modo, encoding="utf-8")
nombre = input("Ingrese el nombre de un avión: ")
peso = int(input("Ingrese el peso del avión: "))
velocidad = float(input("Velocidad maxima:"))
fp.write(nombre+"\n")
fp.write(str(peso)) #Los argumentos de write deben ser str
fp.write("\n")
fp.write(str(velocidad))
#fp.write(nombre+"\n"+peso+"\n"+velocidad)
fp.close()
