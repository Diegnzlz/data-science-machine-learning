# 🟩 Día 1 – NumPy Básico

Ejercicios y mini-reto para dominar NumPy, la librería base de arrays y cálculo numérico en Python.  
Forma parte de la Fase 2 del curso Data Science & Machine Learning.

---

## 🚀 ¿Por qué NumPy?

NumPy es fundamental para ciencia de datos, machine learning y especialmente aprendizaje profundo (deep learning), ya que permite operar de manera eficiente con grandes cantidades de datos y matrices multidimensionales, base para redes neuronales y procesamiento de imágenes.

---

## 📚 Comandos y operaciones más usados en NumPy

| Comando                           | ¿Qué hace?                            | Ejemplo                                  |
|------------------------------------|---------------------------------------|------------------------------------------|
| `np.array([1,2,3])`               | Crea un array                         | `a = np.array([1,2,3])`                  |
| `np.arange(0, 10, 2)`             | Rango de números                      | `np.arange(0,10,2)`                      |
| `np.zeros((n,m))`                 | Array de ceros (n x m)                | `np.zeros((2,3))`                        |
| `np.ones((n,m))`                  | Array de unos                         | `np.ones((3,2))`                         |
| `np.eye(3)`                       | Matriz identidad (3x3)                |                                          |
| `np.random.rand(2,3)`             | Array aleatorio [0,1)                 |                                          |
| `np.random.randn(3,3)`            | Normal estándar (media 0, desv 1)     |                                          |
| `np.random.randint(10,100,(2,5))` | Enteros aleatorios en rango            |                                          |
| `a.shape`                         | Dimensión del array                   |                                          |
| `a.dtype`                         | Tipo de dato                          |                                          |
| `a.reshape((n,m))`                | Cambia la forma del array             |                                          |
| `a.T`                             | Transpone (filas ↔ columnas)          |                                          |
| `a.flatten()`                     | Aplana matriz multidimensional        |                                          |
| `np.concatenate([a, b], axis=0)`  | Une arrays                            |                                          |
| `np.sum(a)`, `np.mean(a)`         | Suma, promedio                        |                                          |
| `np.max(a)`, `np.min(a)`          | Máximo, mínimo                        |                                          |
| `np.dot(a, b)`                    | Producto punto (matricial)            |                                          |
| `np.argmax(a)`, `np.argmin(a)`    | Índice del valor máximo/mínimo        |                                          |
| `a[a > x]`                        | Filtra valores por condición          |                                          |
| `np.linalg.inv(a)`                | Inversa de matriz (Deep Learning)     |                                          |
| `np.linalg.det(a)`                | Determinante de matriz                |                                          |

> ⚡ **Tip**: En aprendizaje profundo (deep learning), NumPy es esencial para inicializar pesos, multiplicar matrices (operaciones tensoriales), normalizar datos y preparar entradas para redes neuronales.

---

## 📝 ¿Qué contiene este archivo?

- Creación y manipulación de arrays
- Operaciones matemáticas básicas y avanzadas
- Ejemplo de slicing, reshape, transposición
- Generación de números aleatorios
- Mini reto de filtrado y estadísticas
- Resumen de propiedades de arrays (`shape`, `dtype`)

---

## 🛠️ ¿Cómo ejecutar?

1. Instala NumPy si no lo tienes:
pip install numpy
2. Ejecuta los ejercicios:
python ejercicios_numpy.py

*Realizado por Diego González — 2025*
