import pandas as pd

# Leer y explorar un CSV

df = pd.read_csv("fase-2-ciencia-de-datos/dia2-pandas-dataframes/personas.csv")
print("Primeras filas:\n", df.head())
print("Columnas:", df.columns)
print("Info:\n", df.info())
print("Estadísticas básicas:\n", df.describe())

# Seleccionar y filtrar datos

print("Solo nombres y ciudad:")
print(df[['nombre', 'ciudad']])

print("Filtrar Maracay:")
print(df[df['ciudad'] == "Maracay"])

print("Edades mayores a 25:")
print(df[df['edad'] > 25])

# Ordenar y resumir
print("Ordenado por nota descendente:")
print(df.sort_values('nota', ascending=False))

print("Promedio de edad:", df['edad'].mean())

# Mini reto del día
# Filtra todas las personas con nota mayor a 18.
# Muestra cuántos hay por cada ciudad (pista: value_counts()).
# Muestra solo el nombre de la persona con mayor edad.

print("Personas con nota mayor a 18:")
nota_mayor_18 = df[df['nota'] > 18]
print(nota_mayor_18)

print("Cantidad por ciudad:")
print(df['ciudad'].value_counts())
print("Nombre de la persona con mayor edad:")
print(df.loc[df['edad'].idxmax(), 'nombre'])
