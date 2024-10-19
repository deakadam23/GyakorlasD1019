import math
def ot():
    szam = int(input("Kérem adjon meg egy 40 és 90 közötti számot"))
    if szam < 40 and szam > 95:
        print("Hiba nem megfelelo szam")
    else:
        szam = str(szam)
        print(szam[0])
        szam = int(szam)
        print(int(szam/10))

        szam = int(szam)
        print(str(math.floor(szam/10)))

    ot()