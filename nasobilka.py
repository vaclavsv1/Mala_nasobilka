import random 

def nasobeni(x, y):
    vysledek = x * y
    return vysledek

pocet_spravnych_odpovedi = 0
if uzivatel == spravna:
        pocet_spravnych_odpovedi += 1

def vyhodnoceni(vysledek, porovnani):
    odpoved = False
    if vysledek == porovnani:
        print("Máš to správně , jsi šikulka")
        odpoved = True
    else:
        print("Ahh , máš to špatně")
    return odpoved

for x in range(10):
    x = random.randint(0,10)
    y = random.randint(0,10)

    porovnani = int(input(f"{x} * {y} = "))
    vysledek = int(nasobeni(x, y))
    vyhodnoceni(vysledek, porovnani)
else:
    print("Počet správných odpovědí je: {pocet_spravnych_odpovedi}/10")