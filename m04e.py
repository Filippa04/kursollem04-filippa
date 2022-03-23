# funktion omkrets
# inparameter: sida1 & sida2
# returvärde inget
def omkrets(s1, s2):
    print("Omkretsen av en rektangel med sidorna {} och {} är {}"
           .format(s1, s2, 2*(s1+s2)))

# funktion omkrets_retur
# inparameter: sida1 & sida2
# returvärde: omkretsen
def omkrets_retur(s1, s2):
    return 2*(s1+s2)

sida1 = 5
sida2 = 5

# ta emot det returnerade värdet
o = omkrets_retur(sida1, sida2)

# Anropar funktionen omkrets för utskrift
omkrets(sida1, sida2)

# Anropar funktionen omkrets_retur i utskriften
print("Omkretsen av en rektangel med sidorna {} och {} är {}"
       .format(sida1, sida2, omkrets_retur(sida1, sida2)))