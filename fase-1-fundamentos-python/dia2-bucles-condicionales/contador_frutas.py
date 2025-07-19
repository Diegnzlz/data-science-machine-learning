lista_de_frutas = ["manzana", "banana", "naranja", "pera", "uva"]

print("\n*** Contador de Frutas ***")
for fruta in lista_de_frutas:
    cantidad_a = fruta.lower().count('a')
    tipo = "Vocal" if fruta[0].lower() in 'aeiou' else "Consonante"
    print(f"{fruta.capitalize()}: tiene {cantidad_a} 'a' - empieza con {tipo}")

# Total de frutas que contienen la letra 'a'
total_con_a = sum(1 for fruta in lista_de_frutas if 'a' in fruta.lower())
print(f"\nTotal de frutas con 'a': {total_con_a}")
