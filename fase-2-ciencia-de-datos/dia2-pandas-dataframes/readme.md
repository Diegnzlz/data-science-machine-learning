# 🟦 Día 2 – Pandas Básico: DataFrames y Manipulación Simple

Ejercicios prácticos y mini-reto para dominar Pandas, la herramienta principal para análisis de datos tabulares en Python.

---

## 🚀 ¿Por qué Pandas?

Pandas es fundamental en ciencia de datos y Machine Learning porque permite cargar, explorar, limpiar, transformar y analizar grandes volúmenes de datos con facilidad. Es el puente entre los datos crudos (CSV, Excel, SQL) y los modelos de aprendizaje automático.

---

## 📚 Comandos y operaciones más comunes en Pandas

| Comando                                 | ¿Qué hace?                                     | Ejemplo                               |
|------------------------------------------|------------------------------------------------|---------------------------------------|
| `pd.read_csv('archivo.csv')`             | Leer CSV como DataFrame                        | `df = pd.read_csv('personas.csv')`    |
| `df.head()`                             | Primeras 5 filas                               |                                       |
| `df.tail()`                             | Últimas 5 filas                                |                                       |
| `df.columns`                            | Lista de nombres de columnas                   |                                       |
| `df.info()`                             | Info general y tipos de datos                  |                                       |
| `df.describe()`                         | Estadísticas básicas de columnas numéricas      |                                       |
| `df['col']`, `df[['col1','col2']]`      | Selección de columna(s)                        |                                       |
| `df.iloc[0]`, `df.iloc[2:5]`            | Selección por posición                         |                                       |
| `df.loc[0, 'col']`                      | Selección por etiqueta                         |                                       |
| `df[df['ciudad'] == 'Maracay']`         | Filtrar por condición                          |                                       |
| `df['edad'].mean()`, `df['nota'].max()` | Estadísticas de columna                        |                                       |
| `df.value_counts()`                      | Conteo por categorías (ideal para clasificación) |                                     |
| `df.sort_values('edad', ascending=False)`| Ordenar DataFrame                              |                                       |
| `df.isnull().sum()`                      | Contar valores nulos                           |                                       |

> ⚡ **En Machine Learning**: Pandas permite preparar, limpiar y transformar datos antes de alimentar modelos de ML/IA (¡paso esencial para buenos resultados!).

---

## 📝 ¿Qué contiene este archivo?

- Lectura y exploración de un archivo CSV con Pandas
- Selección y filtrado de datos relevantes
- Estadísticas básicas y operaciones de resumen
- Mini-reto resuelto:  
  - Filtrar personas con nota > 18  
  - Contar personas por ciudad  
  - Hallar el nombre de la persona con mayor edad

---

## 🛠️ ¿Cómo ejecutar?

1. Instala pandas si no lo tienes:
pip install pandas
2. Ejecuta los ejercicios:
python ejercicios_pandas_1.py

---

*Realizado por Diego González — 2025*
