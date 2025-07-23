import pandas as pd

# Crear DataFrame manualmente y agregar columna

data = {
    'producto': ['Laptop', 'Mouse', 'Teclado'],
    'precio': [1200, 25, 50]
}
df = pd.DataFrame(data)
df['iva'] = df['precio'] * 0.16
print(df)

# Filtrar varias condiciones y reemplazar valores

# Filtrar productos con precio mayor a 30 y que no sean 'Laptop'
filtro = (df['precio'] > 30) & (df['producto'] != 'Laptop')
print(df[filtro])

# Reemplazar valor
df['producto'] = df['producto'].replace('Mouse', 'Ratón')
print(df)

# Agregar nueva fila

nuevo = pd.DataFrame([{'producto': 'Monitor', 'precio': 250, 'iva': 250*0.16}])
df = pd.concat([df, nuevo], ignore_index=True)
print(df)

# Eliminar columnas y filas
# Eliminar columna 'iva'
df_sin_iva = df.drop('iva', axis=1)
print(df_sin_iva)

# Eliminar fila por índice
df_sin_fila = df.drop(0)
print(df_sin_fila)

# Detección de duplicados y nulos

# Las dobles llaves lo dejan como DataFrame, no como Serie
fila_duplicada = df.iloc[[0]]
df_duplicados = pd.concat([df, fila_duplicada], ignore_index=True)
print(df_duplicados.duplicated())

# Crear valor nulo
df_nulos = df.copy()
df_nulos.loc[1, 'precio'] = None
print(df_nulos.isnull().sum())
