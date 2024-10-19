import math
def negy ():
 n =1
 k =1
 if (k%2 == 1) and (n > 0) and (math.pow(2,n)>k):
     print("Proth számok:  ", end= "")
     for n in range(0,10,1):
         proth = (k * math.pow(2,n)) + 1
         print(str(proth)+",")
         proth = (k* math.pow(2,10)) +1
         print(proth)
 else:
  print("HIBA NEM MEGFELELO SZAMOK")

def negyb():
    n = 1
    k = 1
    print("Proth számok:  ", end="")
    while n>10:
        proth = (k * math.pow(2, n)) + 1
        print(str(proth) + ",")
        proth = (k * math.pow(2, 10)) + 1
        print(proth)