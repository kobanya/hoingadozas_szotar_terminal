import random
from tabulate import tabulate

# Paraméterezett változók:
honapok = {
    'Január': [31, 31, -5, 10],   # az ELSŐ két szám a hónap napjainak lehetséges száma
    'Február': [28, 29, -5, 10],   # a MÁSODIK két szám az adott hónapban generálható hőmérséklet hatara
    'Március': [31, 31, 0, 15],
    'Április': [30, 30, 5, 30],
    'Május': [31, 31, 5, 30],
    'Június': [30, 30, 10, 30],
    'Július': [31, 31, 15, 35],
    'Augusztus': [31, 31, 15, 35],
    'Szeptember': [30, 30, 10, 30],
    'Október': [31, 31, 5, 20],
    'November': [30, 30, -5, 10],
    'December': [31, 31, -5, 5]
}

homersekletek = []   # üres lista létrehozása

# függvények
# szökőév ellenőrzése
def szokoev(ev):
    return ev % 4 == 0 and (ev % 100 != 0 or ev % 400 == 0)

# év generálása
ev = random.randint(1900, 2023)

# hónap kiválasztása és a napok számának meghatározása
honap_neve = random.choice(list(honapok.keys()))  # szótár (szópár) használata
if honap_neve == 'Február':   # ha a generált (választott ) hónap február
    if szokoev(ev):            # megnézzük szökőév-e
        napok_szama = honapok[honap_neve][1]  # ha szökőév akkor az ELSŐ értéket veszi fel =29
    else:
        napok_szama = honapok[honap_neve][0] # ha nem szökőév akkor a NULLADIK értéket kapja ami 28
else:
    napok_szama = honapok[honap_neve][0]  # egyéb esetben  28

# hőmérsékletek generálása és tárolása
for i in range(napok_szama):   # napok száma függvényében generálunk hőmérsékletet
    min_hofok = random.randint(honapok[honap_neve][2], honapok[honap_neve][3]) # Megkeresi a hónap nevét és a megadott paramétereket
    max_hofok = random.randint(min_hofok, honapok[honap_neve][3])  # # Megkeresi a hónap nevét és a megadott paramétereket
    homersekletek.append([min_hofok, max_hofok]) # listához adja a generált értékeket

# táblázat kiíratása
print(f'{ev} {honap_neve} hőmérsékletei:') # ellenőrzésnek készült tesztadat
table = [['Év', 'Hónap', 'Nap', 'Min.', 'Max.', 'Ingadozás']] # táblázat fejléce
for i, homerseklet in enumerate(homersekletek): # naok sorszáma
    nap = i + 1 # hogy ne legyen 0. nap
    min_hofok, max_hofok = homerseklet # amin és max hőmérsékleteket elmentjuk egy változóba
    ingadozas = max_hofok - min_hofok # különbség  kiszámítása
    table.append([str(ev), honap_neve, str(nap), str(min_hofok), str(max_hofok), str(ingadozas)]) # tablázatba mentjuk

print('')
print(tabulate(table, headers='firstrow', tablefmt='psql')) # kiírjuk a táblázatot
print('')