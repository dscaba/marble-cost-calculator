# Importamos la librería pandas
import pandas as pd

# Comprobamos la existencia del archivo "marble.csv"
try:
    df = pd.read_csv("marble.csv")

# Si el programa no encuentra el archivo "marble.csv", lo creará automáticamente con las columnas ya establecidas
except:

    df = pd.DataFrame({"Nombre": [" "], "Precio": [" "]})
    df.to_csv("marble.csv")


def add():
    nombre = input("Ingrese nombre: ")
    precio = input("Ingrese precio: ")
    output = pd.DataFrame({"Nombre": [nombre], "Precio": [precio]})
    final = pd.concat([df, output], join="inner")
    final.reset_index(inplace=True)
    final.to_csv("marble.csv")


add()


def delete():
    label = int(input("Ingrese el número del elemento a borrar: "))
    eraser = df.drop(df.index[[label]], inplace=True)
    df.to_csv("marble.csv")


# delete()

print(df)