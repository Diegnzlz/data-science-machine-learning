import operaciones


def main():
    print("*** Calculadora de Operaciones Básicas ***")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Selecciona una opción (1-4): ")

    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == '1':
            resultado = operaciones.sumar(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcion == '2':
            resultado = operaciones.restar(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcion == '3':
            resultado = operaciones.multiplicar(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcion == '4':
            resultado = operaciones.dividir(num1, num2)
            print(f"Resultado: {resultado}")
    else:
        print("Opción no válida. Por favor, selecciona una opción entre 1 y 4.")


main()
