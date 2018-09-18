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
    

aantal_GTCA = sequentie.count("G") + sequentie.count("T") + sequentie.count("C") + sequentie.count("A")
aantal_GC = sequentie.count("G") + sequentie.count("C")
aantal_DERK = sequentie.count("D") + sequentie.count("E") + sequentie.count("R") + sequentie.count("K")
lengte= len(sequentie)

print("""
De lengte van de sequentie is
"""+str(lengte) +""".
""")

if str(header[17]) == "p":
    print("""Het aantal aminozuren D, E, R & K in de sequentie bedraagt:
"""+str(aantal_DERK)+""".
"""+"""
Het percentage DERK ten opzichte van de gehele sequentie bedraagt:
"""+str((int(aantal_DERK)/int(lengte))*100)+"""
""")
    
elif str(header[18]) == "p":
    print("""Het aantal aminozuren D, E, R & K in de sequentie bedraagt:
"""+str(aantal_DERK)+""".
"""+"""
Het percentage DERK ten opzichte van de gehele sequentie bedraagt:
"""+str((int(aantal_DERK)/int(lengte))*100)+"""
""")
    
vergelijken = input("Wil je de lengte van de sequentie vergelijken met een andere sequentie? (y/n):")

if vergelijken == str("y"):
    print("Yes, kies nu het bestand waarmee je de huidige sequentie wilt vergelijken.")
else:
    import sys
    sys.exit()

bestand2 = open(askopenfilename(),"r")

sequentie2= ""
for line in bestand2:
    if line.startswith(">"):
        header2 = line
    if not line.startswith(">"):
        sequentie2 = sequentie2 + line

sequentie2 = sequentie2.replace('\n','').replace('\r', '')

lengte2= len(sequentie2)
lengteverschil = int(lengte) - int(lengte2)

print("""
De lengte van de eerst gegeven sequentie is """+str(lengte)+""".
De lengte van de tweede gegeven sequentie is """+str(lengte2)+""".
Het verschil in lengte is """+str(lengteverschil)+".")
