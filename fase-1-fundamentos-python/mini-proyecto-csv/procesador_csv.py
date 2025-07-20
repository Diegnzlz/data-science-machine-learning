import csv
from collections import Counter
import os


def cargar_datos_csv(ruta_archivo):
    """Carga datos desde un archivo CSV con manejo de errores"""
    try:
        with open(ruta_archivo, newline='', encoding='utf-8') as archivo:
            return list(csv.DictReader(archivo))
    except FileNotFoundError:
        print(f"Error: Archivo '{ruta_archivo}' no encontrado")
        return []
    except Exception as e:
        print(f"Error al leer archivo: {e}")
        return []


def mostrar_personas(personas):
    """Muestra personas en formato tabular"""
    if not personas:
        print("No hay datos para mostrar")
        return

    headers = personas[0].keys()
    print(
        "\n".join([f"{k}: {v}" for persona in personas for k, v in persona.items()]))
    print("-" * 30)


def buscar_personas(datos, campo, valor):
    """Busca personas por cualquier campo con coincidencia parcial"""
    return [p for p in datos if valor.lower() in p[campo].lower()]


def obtener_estadisticas(datos):
    """Calcula estadísticas optimizadas con una sola iteración"""
    if not datos:
        return {}

    total_edad = 0
    total_nota = 0
    ciudades = set()

    for persona in datos:
        total_edad += int(persona['edad'])
        total_nota += float(persona['nota'])
        ciudades.add(persona['ciudad'])

    return {
        'total_personas': len(datos),
        'ciudades_unicas': len(ciudades),
        'promedio_edad': total_edad / len(datos),
        'promedio_nota': total_nota / len(datos),
        'conteo_ciudades': Counter(p['ciudad'] for p in datos)
    }


def menu_principal():
    """Menú interactivo mejorado con nuevas opciones"""
    ruta_base = "fase-1-fundamentos-python/mini-proyecto-csv"
    archivo = input(
        f"Ingrese nombre del archivo (default: personas.csv): ") or "personas.csv"
    ruta_completa = os.path.join(ruta_base, archivo)

    datos = cargar_datos_csv(ruta_completa)
    if not datos:
        return

    estadisticas = None

    while True:
        print("\n" + "=" * 40)
        print("1. Listar todas las personas")
        print("2. Buscar por nombre")
        print("3. Buscar por ciudad")
        print("4. Personas por ciudad (conteo)")
        print("5. Mostrar estadísticas")
        print("6. Actualizar estadísticas")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_personas(datos)

        elif opcion in ("2", "3"):
            campo = "nombre" if opcion == "2" else "ciudad"
            valor = input(f"Ingrese {campo} a buscar: ").strip()
            resultados = buscar_personas(datos, campo, valor)
            mostrar_personas(resultados)

        elif opcion == "4":
            conteo = Counter(p['ciudad'] for p in datos)
            for ciudad, cantidad in conteo.most_common():
                print(f"{ciudad}: {cantidad} persona(s)")

        elif opcion in ("5", "6"):
            if opcion == "6" or estadisticas is None:
                estadisticas = obtener_estadisticas(datos)
            print("\n--- ESTADÍSTICAS ---")
            print(f"Personas registradas: {estadisticas['total_personas']}")
            print(f"Ciudades únicas: {estadisticas['ciudades_unicas']}")
            print(f"Promedio de notas: {estadisticas['promedio_nota']:.2f}")
            print(f"Promedio de edad: {estadisticas['promedio_edad']:.2f}")
            print("\nDistribución por ciudades:")
            for ciudad, cantidad in estadisticas['conteo_ciudades'].most_common():
                print(f"  {ciudad}: {cantidad}")

        elif opcion == "7":
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu_principal()
