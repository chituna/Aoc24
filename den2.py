def isSafe(array):
    safe = True
    klesa = True
    r = array
    #print(r)
    a = int(r.pop(0))
    b = int(r.pop(0))
    # print("a,b", a, b)

    if (a - b) in stoupajici:
        klesa = False
    elif (a - b) in decreasing:
        klesa = True
    else:
        safe = False

    while len(r) > 0 and safe:
        a = int(b)
        b = int(r.pop(0))
        if klesa:
            if (a - b) not in decreasing:
                safe = False
        else:
            if (a - b) not in stoupajici:
                safe = False

    return safe


stoupajici = {1, 2, 3}
decreasing = {-1,-2,-3}
chyb = 0
unsafe = []
with (open("vstup2.txt") as soubor):
    suma = 0
    for radek in soubor:
        predek = []
        safe = True
        klesa = True
        radek.strip()
        r = radek.strip().split(" ")
        #print("radek: ", r)
        a = int(r.pop(0))
        b = int(r.pop(0))
        #print("a,b", a, b)

        if (a-b) in stoupajici:
            klesa = False
        elif (a-b) in decreasing:
            klesa = True
        else:
            safe = False

        while len(r) > 0 and safe:
            a = int(b)
            b = int(r.pop(0))
            if klesa:
                if (a-b) not in decreasing:
                    safe = False
            else:
                if (a-b) not in stoupajici:
                    safe = False
        #print(radek.strip().split(" "))
        #print("je to safe", isSafe(radek.strip().split(" ")))
        if safe:
            suma += 1
            #print("safe")

        else:
            jeSafe = False
            for i in range(len(radek.strip().split(" "))):
                ar = radek.strip().split(" ")
                #print("tady hledam chybu", ar)
                ar.remove(ar[i])
                kopie = list(ar)
                #print("tady hledam chybu222", ar)
                #print(ar, "array je ar", isSafe(ar))
                if isSafe(ar):
                    jeSafe = True
                    #print("safe s ubranim*******", kopie)

            if jeSafe:
                suma += 1
                #print("safe na druhou")
            else:
                #print(radek)
                unsafe.append(radek.strip().split(" "))




print("suma", suma)
print(unsafe)
seznam = []
duplicity = []
for u in unsafe:
    delkaSet = len(set(u))
    delkaSez = len(u)
    #print(delkaSet, delkaSez, "delky")
    if delkaSet == delkaSez: #or delkaSet+1 == delkaSez:
        seznam.append(list(map(int, u)))
    elif delkaSet+1 == delkaSez:
        duplicity.append(list(map(int, u)))



print(*seznam)
print(len(seznam))
for s in duplicity:
    print(*s)

print(len(duplicity))
