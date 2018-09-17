from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
bestand = open(askopenfilename(),"r")

sequentie= ""
for line in bestand:
    if line.startswith(">"):
        header = line
    if not line.startswith(">"):
        sequentie = sequentie + line

sequentie = sequentie.replace('\n','').replace('\r', '')
print("""
                                   HEADER
--------------------------------------------------------------------------------
"""+str(header))
print("""
                                   SEQUENTIE
--------------------------------------------------------------------------------
"""+str(sequentie)+"""
""")

if str(header[12]) == ":":
    print("Dit is een DNA-sequentie.")
elif str(header[13]) == ":":
    print("Dit is een DNA-sequentie.")
elif str(header[17]) == "p":
    print("Dit is een Eiwitsequentie.")
elif str(header[18]) == "p":
    print("Dit is een Eiwitsequentie.")
else:
    print("Dit is een mRNA-sequentie.")
    

lengte = len(sequentie)
aantal_GTCA = sequentie.count("G") + sequentie.count("T") + sequentie.count("C") + sequentie.count("A")
aantal_GC = sequentie.count("G") + sequentie.count("C")
aantal_DERK = sequentie.count("D") + sequentie.count("E") + sequentie.count("R") + sequentie.count("K")
vergelijken = "n"

print("De lengte van de sequentie is "+str(lengte) +""".
""")

if str(header[17]) == "p":
    print("Het aantal aminozuren D, E, R & K in de sequentie bedraagt: "+str(aantal_DERK)+""".
""")
elif str(header[18]) == "p":
    print("Het aantal aminozuren D, E, R & K in de sequentie bedraagt: "+str(aantal_DERK)+""".
""")
else:
    print("")

vergelijken = input("Wil je de lengte van de mRNA-sequentie vergelijken met de eiwit-sequentie? (y/n):")

if vergelijken == str("y"):
    print("Yes, kies nu het bestand waarmee je de huidige sequentie wilt vergelijken.")
else:
    import sys
    sys.exit()

bestand2 = open(askopenfilename(),"r")
