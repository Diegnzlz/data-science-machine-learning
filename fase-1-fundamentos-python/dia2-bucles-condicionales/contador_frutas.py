lista_de_frutas = ["manzana", "banana", "naranja", "pera", "uva"]
contador_frutas = {}


def contar_frutas():
    for fruta in lista_de_frutas:
        if fruta in contador_frutas:
            contador_frutas[fruta] += 1
        else:
            contador_frutas[fruta] = 1

    print("\n*** Contador de Frutas ***")
    for fruta, cantidad in contador_frutas.items():
        print(f"{fruta.capitalize()}: {cantidad}")


def frutas_con_a():
    print("\n*** Frutas que contienen la letra 'a' ***")
    for fruta in lista_de_frutas:
        if 'a' in fruta.lower():
            print(fruta.capitalize())


def vocal_consonante():
    print("\n*** Frutas que empiezan con vocal o consonante ***")
    for fruta in lista_de_frutas:
        if fruta[0].lower() in 'aeiou' or fruta[0].lower() in 'bcdfghjklmnpqrstvwxyz':
            print(fruta.capitalize(), "- Empieza con:",
                  "Vocal" if fruta[0].lower() in 'aeiou' else "Consonante")


contar_frutas()
frutas_con_a()
vocal_consonante()
