import numpy as np

# | Comando                   | ¿Qué hace?                            | Ejemplo                 |
# | ------------------------- | ------------------------------------- | ----------------------- |
# | `np.array([1,2,3])`       | Crea un array                         | `a = np.array([1,2,3])` |
# | `np.arange(0, 10, 2)`     | Rango de números                      | `np.arange(0,10,2)`     |
# | `np.zeros((2,3))`         | Array de ceros                        | `np.zeros((2,3))`       |
# | `np.ones((3,2))`          | Array de unos                         | `np.ones((3,2))`        |
# | `np.shape`                | Tamaño del array                      | `a.shape`               |
# | `a[0]`, `a[1:3]`          | Indexar/slicear arrays                |                         |
# | `np.sum(a)`, `np.mean(a)` | Suma, media de los valores            |                         |
# | `np.max(a)`, `np.min(a)`  | Máximo, mínimo                        |                         |
# | `a.T`                     | Transponer (cambiar filas x columnas) |                         |
# | `np.random.rand(3,2)`     | Array aleatorio (valores 0 a 1)       |                         |
# | `a.reshape((n, m))`       | Cambiar forma                         |                         |
# | `a * 2`, `a + 3`          | Operaciones vectorizadas              |                         |


# ejercicios básicos de numpy
a = np.array([2, 4, 6, 8])
print("Array:", a)
print("Suma:", np.sum(a))
print("Media:", np.mean(a))
print("Máximo:", np.max(a))
print("Mínimo:", np.min(a))

ceros = np.zeros((3, 2))
unos = np.ones((2, 3))
aleatorios = np.random.rand(2, 4)

print("Ceros:\n", ceros)
print("Unos:\n", unos)
print("Aleatorios:\n", aleatorios)

b = np.arange(10)  # [0 1 2 ... 9]
print("b[2:7]:", b[2:7])
print("b * 3:", b * 3)
print("b + 1:", b + 1)

m = np.arange(6).reshape((2, 3))
print("Matriz:\n", m)
print("Transpuesta:\n", m.T)

# mini reto
# Crea un array de 20 números aleatorios entre 10 y 100 (usa np.random.randint),
# imprime el array, la suma, el valor máximo, el mínimo, y todos los valores mayores a 50.
print("Mini reto:")
array_aleatorio = np.random.randint(10, 101, size=20)
print("Array aleatorio:", array_aleatorio)
print("Suma:", np.sum(array_aleatorio))
print("Máximo:", np.max(array_aleatorio))
print("Mínimo:", np.min(array_aleatorio))
print("Valores mayores a 50:", array_aleatorio[array_aleatorio > 50])
# Fin del mini reto
