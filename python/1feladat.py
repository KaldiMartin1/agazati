a = int(input('Kérek egy egész számot: '))
b = int(input('Kérek egy másik egész számot: '))
while a>b:
    print('\tA második számnak nagyobbnak kell lennie az elsőnél!')
    a = int(input('Kérek egy egész számot: '))
    b = int(input('Kérek egy másik egész számot: '))
osszeg = 0
for i in range(a, b+1):
    osszeg += 1
print(f'A két szám közötti egész számok összege: {osszeg}')