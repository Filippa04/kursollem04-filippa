sida1 = int(input("Ange en rektangels ena sida: "))
sida2 = int(input("Ange en rektangels andra sida: "))
area = sida1 * sida2
print("Höjd | Volym")
print("-------------")
for i in range(1, 11):
    print("   {}  |  {}".format(i, area*i))
if sida1 == sida2:
    print("Arean är", area, "cm")
    print("Eftersom båda sidorna är lika långa så är rektangeln en kvadrat")
else:
    print("Arean är", area, "cm")

igen = input("Vill du göra en beräkning till? (ja/nej)")

if igen == "ja":
    side1 = int(input("Ange rektangelns enda sida: "))
    side2 = int(input("Ange rektangelns andra sida: "))
    area2 = side1 * side2
    print("Höjd | Volym")
    print("-------------")
    for i in range(1, 11):
        print("   {}  |  {}".format(i, area2*i))
    if igen == "nej":
        print("Arean är", area, "cm")

else:
    print("Arean är", area, "cm")

print("Dina figurer är följande: ")
sidan1 = []
sidan2 = []
sidan1.append(side1)
print(sidan1)
sidan2.append(sida2)
print(sidan2)
for i in (sidan1, sidan2):
    print(sidan1, sidan2)
