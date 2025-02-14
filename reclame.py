from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    print(f"emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {str(prijs-(prijs*korting)) + "0"} euro.")
aanbieding_1("aardbei", 4, 0.1)

def inkomsten_totaal(inkomsten,btw=0.09):
    totaal=0
    for i in range(len(inkomsten)):
        totaal=totaal+inkomsten[i]
    print(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {totaal*btw} euro btw betaald dient te worden")
inkomsten_totaal([220, 430, 125, 160, 205, 90, 345])

def laag_en_hoog(mijn_lijst):
    uitvoer = max(mijn_lijst), min(mijn_lijst)
    return uitvoer

def gemiddelde(mijn_lijst):
    tot=0
    for i in range(len(mijn_lijst)):
        tot = tot + mijn_lijst[i]
    gem = tot / len(mijn_lijst)
    print(f"De gemiddelde inkomsten deze week zijn {gem} euro.")
gemiddelde([220, 430, 125, 160, 205, 90, 345])

def meervoudig(invoer_lijst):
    uitvoer = laag_en_hoog(invoer_lijst)
    return uitvoer
meervoudig([10, 5, 3, 2, 1, 2, 9])

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
combinatie([10, 5, 3, 2, 1, 2, 9])
