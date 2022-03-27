lista_slow = ["ogary", "poszły", "w", "las"]

zdanie = " ".join(lista_slow).capitalize() + str('.')

print(zdanie)

zdanie2 = "A to nam zabili Ferdynanda."

lista_slow2 = [word[:-1].lower() if word.endswith('.') else word.lower() for word in zdanie2.split()]

print(lista_slow2)
