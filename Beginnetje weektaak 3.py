while 1:

    Sequentie = input("Voer hier uw sequentie in (in HOOFDLETTERS): ")
    Lengte = len(Sequentie)
    Aantal_GTCA = Sequentie.count("G") + Sequentie.count("T") + Sequentie.count("C") + Sequentie.count("A")
    Aantal_GC = Sequentie.count("G") + Sequentie.count("C")
    Aantal_DERK = Sequentie.count("D") + Sequentie.count("E") + Sequentie.count("R") + Sequentie.count("K")

    if int(Lengte) > int(Aantal_GTCA):
        print("""
Dit is een Eiwit Sequentie
""")
    else:
        print("""
Dit is een DNA of RNA sequentie
""")

    print("De lengte van de sequentie is "+str(Lengte) +"""
""")

    if int(Lengte) > int(Aantal_GTCA):
         print("Het aantal aminozuren D, E, R & K in de sequentie bedraagt: "+str(Aantal_DERK)+"""
""")
    else:
        print("")


    Vergelijken = input("Wil je de lengte van de mRNA-sequentie vergelijken met de eiwit-sequentie? (y/n): ")
    if Vergelijken == str("y"):
        Eiwitsequentie = input("Voer hier de Eiwit-sequentie in: ")
        Eiwitlengte = len(Eiwitsequentie)
        Lengteverschil = int(Lengte) - int(Eiwitlengte)
        print("De lengte van de mRNA-sequentie is "+str(Lengte)+"""
De lengte van de Eiwit-sequentie is """+str(Eiwitlengte)+"""
Het verschil in lengte is """+str(Lengteverschil))
    
        




    print("""
--------------------------------------------------------------""")
