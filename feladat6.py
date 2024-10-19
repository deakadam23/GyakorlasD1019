def beolvas():
    oldal = input("Add meg a háromszög oldalát")
    return oldal




def hat():
    a = beolvas()
    b = beolvas()
    c = beolvas()
    if(a>0 and b > 0 and c> 0):
        if a<c+b and c<b+c and b<a+c:
            print("A háromszög megszerkeszthető")
        else:
            print("A háromszög nem megszerkeszthető")
        pass
    else:
        print("Hiba! Nem megfelelo adatok")

    hat()