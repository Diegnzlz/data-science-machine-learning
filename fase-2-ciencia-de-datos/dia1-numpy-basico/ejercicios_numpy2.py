import numpy as np

# Operaciones entre matrices y producto

a = np.array([[1, 2], [3, 4]])
b = np.array([[2, 0], [1, 2]])

# Suma elemento a elemento
print("Suma:\n", a + b)

# Multiplicación elemento a elemento
print("Multiplicación:\n", a * b)

# Producto punto (matricial)
print("Producto matricial:\n", np.dot(a, b))

# Estadísticas por filas y columnas
m = np.random.randint(1, 10, (4, 4))
print("Matriz:\n", m)
print("Media por fila:", m.mean(axis=1))
print("Media por columna:", m.mean(axis=0))

# Indexación booleana avanzada
arr = np.arange(10)
pares = arr[arr % 2 == 0]
print("Solo pares:", pares)

# Normalización de datos (muy usado en Deep Learning)
datos = np.random.randint(20, 100, 10)
normalizado = (datos - np.min(datos)) / (np.max(datos) - np.min(datos))
print("Datos:", datos)
print("Normalizados:", normalizado)
