with (open("vstup2.txt") as soubor):
    suma = 0
    increasing = {-1, -2, -3}  # 1,2,3,4
    decreasing = {1, 2, 3}
    for radek in soubor:
        r = list(map(int, radek.strip().split(" ")))

        rozdily = []
        for i in range(len(r)-1):
            rozdily.append(r[i]-r[i+1])

        roz = set(rozdily)

        if roz.issubset(increasing) or roz.issubset(decreasing):
            suma += 1

        else:
            jeSafe = False
            for i in range(len(r)):
                ar = list(r)
                ar.pop(i)

                rozdily2 = []
                for j in range(len(ar) - 1):
                    rozdily2.append(ar[j] - ar[j + 1])

                print(rozdily2)
                roz2 = set(rozdily2)

                if roz2.issubset(increasing) or roz2.issubset(decreasing):
                    jeSafe = True

            if jeSafe:
                suma += 1

    print("suma", suma)