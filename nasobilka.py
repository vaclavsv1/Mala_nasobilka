import random 

def nasobeni(x, y):
    vysledek = x * y
    return vysledek

def vyhodnoceni(vysledek, porovnani):
    odpoved = False
    if vysledek == porovnani:
        print("Máš to správně , jsi šikulka!")
    else:
        print("Ahh , špatně")
    return odpoved

for x in range(11):
    x = random.randint(0,10)
    y = random.randint(0,10)

    porovnani = input(f"{x} * {y} = ")