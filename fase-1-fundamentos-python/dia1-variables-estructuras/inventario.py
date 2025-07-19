# inventario.py - Versión mejorada

inventario = {
    "cafe": 10,
    "pan": 5,
    "azucar": 7
}


def mostrar_inventario():
    if not inventario:
        print("Inventario vacío.")
        return
    print("\n*** Inventario Actual ***")
    for producto, cant in inventario.items():
        print(f"- {producto.capitalize()}: {cant}")
    print()


def agregar_producto():
    nombre = input("Nombre del producto a agregar: ").strip().lower()
    if not nombre:
        print("Nombre no puede estar vacío.")
        return
    try:
        cantidad = int(input("Cantidad a agregar: "))
        if cantidad <= 0:
            raise ValueError
    except ValueError:
        print("La cantidad debe ser un número entero mayor que cero.")
        return

    inventario[nombre] = inventario.get(nombre, 0) + cantidad
    print(
        f"{cantidad} unidad(es) agregada(s) a '{nombre}'. Nueva cantidad: {inventario[nombre]}")


def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ").strip().lower()
    if inventario.pop(nombre, None) is not None:
        print(f"Producto '{nombre}' eliminado.")
    else:
        print(f"No se encontró '{nombre}' en el inventario.")


def modificar_cantidad():
    nombre = input("Nombre del producto a modificar: ").strip().lower()
    if nombre not in inventario:
        print(f"'{nombre}' no está en el inventario.")
        return

    try:
        nueva = int(input(f"Nueva cantidad para '{nombre}': "))
    except ValueError:
        print("La cantidad debe ser un número entero.")
        return

    if nueva <= 0:
        print("La cantidad debe ser mayor que cero.")
    else:
        inventario[nombre] = nueva
        print(f"Nueva cantidad de '{nombre}': {nueva}")
        if nueva < 3:
            print("⚠️ Aviso: cantidad baja, considera reponer.")


def guardar_en_archivo():
    with open("fase-1-fundamentos-python/dia1-variables-estructuras/inventario.txt", "w") as f:
        for prod, cant in inventario.items():
            f.write(f"{prod},{cant}\n")
    print("Inventario guardado en 'inventario.txt'.")


def menu():
    opciones = {
        "1": ("Ver inventario", mostrar_inventario),
        "2": ("Agregar producto", agregar_producto),
        "3": ("Eliminar producto", eliminar_producto),
        "4": ("Modificar cantidad", modificar_cantidad),
        "5": ("Guardar inventario en archivo", guardar_en_archivo),
        "6": ("Salir", None)
    }

    while True:
        print("\n*** MENÚ INVENTARIO ***")
        for k, (desc, _) in opciones.items():
            print(f"{k}. {desc}")
        elec = input("Elige una opción: ").strip()

        if elec == "6":
            print("Saliendo...")
            break
        accion = opciones.get(elec)
        if accion:
            accion[1]()
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
