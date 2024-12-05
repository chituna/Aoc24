import math

with (open("vstup5.txt") as soubor):
    celkem = 0
    prvniCast = True
    rules = []
    pred = {}
    za = {}
    pocetDobre = 0

    for radek in soubor:
        # print("radek.strip",)
        r = radek.strip()
        if r == "":
            prvniCast = False
        elif prvniCast:
            a, b = map(int, r.split("|"))
            #print(a,b)
            if a not in pred.keys():
                pred[a] = [b]
            else:
                #print(type(pred[a]), "pred a", b)
                c = list(pred[a])
                c.append(b)
                #print(c, "cecko")
                pred[a] = c

            if b not in za.keys():
                za[b] = [a]
            else:
                c = list(za[b])
                c.append(a)
                za[b] = c

        #druha cast
        else:
            cisla = list(map(int, r.split(",")))
            #print(cisla)
            stred = math.floor(len(cisla)/2)
            #print(stred, "----------stred --------")
            dobre = True

            for i in range(len(cisla)):
                x = cisla[i]
                for j in range(0,i):
                    #print(" chyba   cisla, x, j", cisla, x, j)
                    y = cisla[j]
                    # kdyz je y v seznamu za a x je tam
                    if y in za.keys():
                        if x in za[y]:
                            dobre = False

                for k in range(i+1, len(cisla)):
                    z = cisla[k]
                    if k in pred.keys():
                        if x in pred[k]:
                            dobre = False

            if dobre:
                #print("je to dobre", cisla, "stred ", cisla[stred])
                celkem += cisla[stred]
                pocetDobre += 1
            else:
                print("jneni to dobre", cisla)



print(pred)
print(za)
zz = list(za.keys())
zz.sort()
pp = list(pred.keys())
pp.sort()
print(pp)
print(zz)

print("celkem", celkem, pocetDobre)
#2120 je malo

print("-----------")
for key, val in pred.items():
    print(key, val)