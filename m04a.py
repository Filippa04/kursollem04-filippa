# skapar input där värden matas in
sida1 = int(input("Ange en rektangels ena sida: "))
sida2 = int(input("Ange en rektangels andra sida: "))
area = sida1 * sida2 # multiplicerar värdena 
# skapar en if sats som säger om värdena skapar en rektangel eller kvadrat
if sida1 == sida2:
    print("Arean är", area, "cm")
    print("Eftersom båda sidorna är lika långa så är rektangeln en kvadrat")
else: # annars räknas bara arean ut. 
    print("Arean är", area, "cm")