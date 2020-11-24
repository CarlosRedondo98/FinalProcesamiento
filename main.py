#Carlos Redondo Hurtado
#carlos.redondo@javeriana.edu.co
#Tarea 1
#C:/Users/carlo/Downloads/flag1

# importar clases
from bandera import *

# Main

if __name__ == "__main__":

    rutaImagen = input("Ingrese la ruta de la imagen: ")
    imagen = bandera(rutaImagen)
    imagen.colores()
