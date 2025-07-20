import csv
from collections import Counter


def cargar_datos_csv(ruta_archivo):
    datos = []
    with open(ruta_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append(fila)
    return datos


def listar_personas(datos):
    for fila in datos:
        print(fila)


def buscar_por_nombre(datos, nombre):
    encontrados = [f for f in datos if f['nombre'].lower() == nombre.lower()]
    if encontrados:
        for f in encontrados:
            print(f)
    else:
        print("no encontrado.")


def personas_por_ciudad(datos):
    ciudades = [fila['ciudad'] for fila in datos]
    conteo = Counter(ciudades)
    for ciudad, cantidad in conteo.items():
        print(f"{ciudad}: {cantidad} persona(s)")


def calcular_estadisticas(datos):
    edades = [int(f['edad']) for f in datos]
    ciudad = [str(f['ciudad']) for f in datos]
    notas = [float(f['nota']) for f in datos]
    promedio_edades = sum(edades) / len(edades)
    promedio_notas = sum(notas) / len(notas)
    promedio_cuidad = len(set(ciudad))  # Cantidad de ciudades únicas
    print(f"Cantidad de personas: {len(datos)}")
    print(f"cantidad de ciudades: {len(set(ciudad))}")
    print(f"Promedio de notas: {promedio_notas:.2f}")
    print(f"Promedio de edad: {promedio_edades:.2f}")
    print(f"Cantidad de ciudades únicas: {promedio_cuidad}")


def menu():
    datos = cargar_datos_csv(
        "fase-1-fundamentos-python/mini-proyecto-csv/personas.csv")
    while True:
        print("\n1. Listar todos\n2. Buscar por nombre\n3. personas por ciudad\n4. Estadísticas\n5. Salir")
        op = input("Opción: ")
        if op == "1":
            listar_personas(datos)
        elif op == "2":
            nombre = input("Nombre a buscar: ")
            buscar_por_nombre(datos, nombre)
        elif op == "3":
            personas_por_ciudad(datos)
        elif op == "4":
            calcular_estadisticas(datos)
        elif op == "5":
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
