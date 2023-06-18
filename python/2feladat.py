def terulet(a,b):
    Terulet=a*b
    if Terulet<100:
        raise ValueError("Hiba: Túl kicsi a telek!")
    return Terulet
print("2. feladat: Terület kiszámítása")

while True:
    a=float(input("Kérem adja meg a telek szélességét: "))
    if a == -1:
        break
    b=float(input("Kérem adja meg a telek hosszúságát: "))
    if b == -1:
        break
    try:
        print(f'A telek területe: {terulet(a, b)}m2')
    except ValueError as error:
        print(error)