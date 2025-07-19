inventario = {
    "manzanas": 50,
    "naranjas": 30,
    "platanos": 20,
    "peras": 15,
    "uvas": 25
}


def mostrar_inventario(inventario):
    print("Inventario actual:")
    for fruta, cantidad in inventario.items():
        print(f"{fruta}: {cantidad} unidades")


def agregar_producto(inventario, fruta, cantidad):
    if fruta in inventario:
        inventario[fruta] += cantidad
    elif fruta not in inventario and cantidad <= 0:
        print("La cantidad debe ser mayor que cero para agregar un nuevo producto.")
        return
    else:
        inventario[fruta] = cantidad
    print(f"Agregado {cantidad} unidades de {fruta} al inventario.")


def eliminar_producto(inventario, fruta, cantidad):
    if fruta in inventario:
        if inventario[fruta] >= cantidad:
            inventario[fruta] -= cantidad
            print(f"Eliminado {cantidad} unidades de {fruta} del inventario.")
            if inventario[fruta] == 0:
                del inventario[fruta]
                print(f"{fruta} ha sido eliminado del inventario.")
        elif inventario[fruta] < cantidad:
            print(
                f"No se puede eliminar {cantidad} unidades de {fruta}. Solo hay {inventario[fruta]} unidades disponibles.")
        else:
            print(f"No hay suficientes unidades de {fruta} para eliminar.")
    else:
        print(f"{fruta} no está en el inventario.")


def modificar_producto(inventario, fruta, nueva_cantidad):
    if fruta in inventario:
        inventario[fruta] = nueva_cantidad
        print(f"{fruta} ha sido modificado a {nueva_cantidad} unidades.")
    elif fruta not in inventario and nueva_cantidad <= 0:
        print("La cantidad debe ser mayor que cero para modificar un producto.")
    elif fruta in inventario and nueva_cantidad <= 3:
        print("el inventario no puede tener menos de 3 unidades de un producto.")
    else:
        print(f"{fruta} no está en el inventario.")


def menu():
    print("\nOpciones del inventario:")
    print("1. Mostrar inventario")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("4. Modificar producto")
    print("5. Salir")


def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_inventario(inventario)
        elif opcion == "2":
            fruta = input("Ingrese el nombre de la fruta a agregar: ")
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            agregar_producto(inventario, fruta, cantidad)
        elif opcion == "3":
            fruta = input("Ingrese el nombre de la fruta a eliminar: ")
            cantidad = int(input("Ingrese la cantidad a eliminar: "))
            eliminar_producto(inventario, fruta, cantidad)
        elif opcion == "4":
            fruta = input("Ingrese el nombre de la fruta a modificar: ")
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            modificar_producto(inventario, fruta, nueva_cantidad)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
