import math

with (open("vstup17.txt") as soubor):
    zmena = True
    register = {}
    programy = []
    for radek in soubor:
        radek = radek.strip()
        if radek == "":
            zmena = False

        elif zmena:
            rrr = radek.split(":")
            r1 = rrr[0].split(" ")
            #print("r1", r1[1])
            c = int(rrr[1])
            #print("c", c)

            register[r1[1]] = c

        else:
            rrr = radek.split(":")

            programy =list(map(int, rrr[1].strip().split(",")))


    pointer = 0
    maxP = len(programy)
    print("kontrola", pointer, maxP)
    combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: register["A"], 5: register["B"], 6: register["C"], 7: 7}
    print(register)
    #ctu, co mam delat
    output = []

    while pointer+1 < maxP:
        opcode = programy[pointer]
        operand = programy[pointer + 1]
        print("opcode", opcode, "operand", operand, combo[operand])
        print("pointer", pointer)
        #pointer +=2
        if opcode == 0:
            value = register["A"]/(2**combo[operand])
            v = math.trunc(value)
            register["A"] = v
            combo[4] = v
            pointer += 2

        elif opcode == 1:
            value = register["B"] ^ operand
            #print(value)
            register["B"] = value
            combo[5] = value
            pointer += 2

        elif opcode == 2:
            value = combo[operand]%8
            register["B"] = value
            combo[5] = value
            pointer += 2

        elif opcode == 3:
            if register["A"] == 0:
                pointer += 2
            else:
                pointer = operand

        elif opcode == 4:
            value = register["B"] ^ register["C"]
            register["B"] = value
            combo[5] = value
            pointer += 2

        elif opcode == 5:
            value = combo[operand]%8
            output.append(value)
            pointer += 2

        elif opcode == 6:
            value = register["A"] / (2 ** combo[operand])
            v = math.trunc(value)
            register["B"] = v
            combo[5] = v
            pointer += 2

        elif opcode == 7:
            value = register["A"] / (2 ** combo[operand])
            v = math.trunc(value)
            register["C"] = v
            combo[6] = v
            pointer += 2



        #print(combo)
        print(register)


    print(output)
    res = ""
    for o in output:
        res += str(o)

    print("vysledek", res)

    #215331511 neni
    #461421316 neni

