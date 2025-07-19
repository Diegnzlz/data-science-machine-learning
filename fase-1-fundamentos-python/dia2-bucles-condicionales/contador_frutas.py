# contador_frutas.py

lista_de_frutas = ["manzana", "banana", "naranja", "pera", "uva"]


def analizar_frutas(frutas):
    total_con_a = 0
    print("\n*** Contador de Frutas ***")
    for fruta in frutas:
        cantidad_a = fruta.lower().count('a')
        if 'a' in fruta.lower():
            total_con_a += 1
        tipo = "Vocal" if fruta[0].lower() in 'aeiou' else "Consonante"
        print(f"{fruta.capitalize()}: tiene {cantidad_a} 'a' - empieza con {tipo}")
    print(f"\nTotal de frutas con 'a': {total_con_a}")


if __name__ == "__main__":
    analizar_frutas(lista_de_frutas)
