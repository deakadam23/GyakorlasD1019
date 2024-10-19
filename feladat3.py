def harom():
 a1 = int(input("Kérem adja meg a számtani sorozat első elemét:"))
 n = int(input("Kérem adja meg a számtani sorozat ellenszámát:"))
 d = int(input("Kérem adja meg a számtani  sorozat differenciajat: "))

 an = a1 +(n-1)*d
 sn = ((a1+an)*n)/2

 print("a1="+str(a1)+"n="+str(n)+" d="+str(d)+ " Sn="+str(sn))
 if d > 0:
    print("A számtani sorozat monoton novekvo es alulrol korlatos")

 elif d < 0:
  print("A számtani sorozat monoton csokkeno, felulrol korlatos")
 else:print("A számtani sorozat nem csokkeno, nem novekvo, azaz allando")

harom()