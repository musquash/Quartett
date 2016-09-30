__author__ = "5369872: julian raab, 4109208: philipp lang"

from implementierung import *


def quartett():

    while True:
       
        number = int(input("Anzahl der Spieler bitte eintragen (2-8): "))

        if number > 8:
                print("FEHLER zu viele Spieler")
        elif number < 2:
            print("FEHLER zu wenig Spieler")
        else:
            print("Okay sie haben nun " + str(number) +" Mitspieler")
            break
        
    Spieler = []
    #Diese Liste beinhaltelt alle Spieler mit deren Informationen
    #Also Spieler = [[Spieler 1], [Speiler 2], ...]
    #Die Elemente [Spieler x] sind ebenfalls Listen:
    #[Spieler x] = [Nummer, Name, Status, Punkte, [Handkarten]]



    for i in range(number):
       x = input("Name von Spieler " + str(i + 1 ) + ": ")
       while True :
           y = input("Ist dieser Spieler ein Computer? (j,n) ")
           if y == "j":
               s = "Computer"
               break
           elif y == "n":
               s = "Human"
               break
           else:
               print("FEHLER")

       
       xliste = [i + 1 , x, s, 0, []] #Habe die leere List hinzugefügt
       Spieler.append(xliste)


    #Verteilung der Karten auf die Spieler (nach Spieleranzahl).
    if(number < 3):
        Spieler_1 = Spieler[0]
        Spieler_2 = Spieler[1]

        give_Cards(10, Spieler_1, Cards)
        give_Cards(10, Spieler_2, Cards)

        Stapel = Cards
    #ab hier habe ich weiter gearbeitet
    else:
        r = len(Cards) % number
        t = int(len(Cards) / number)
        for i in range(number):
            give_Cards(t, Spieler[i], Cards)
            if r > 0:
                Spieler[i][4].append(Cards[0])
                r -= 1
            
    




    for i in range(number):
        print(Spieler[i])

    ##if(number < 3):
    ##    Spieler_1 = Spieler[0]
    ##    Spieler_2 = Spieler[1]
    ##    
    ##    give_Cards(10, Spieler_1, Cards)
    ##    give_Cards(10, Spieler_2, Cards)
    ##
    ##    Stapel = Cards
    ##    
    ##else:
    ##   while i in range(number)):
    ##       Spieler_i=Spieler.index[i]
    ##       Spieler_i.append()
    ##       
    ##   r=1
    ##for 'Handkarten_oder_so' > 0:
    ##    print("Runde "+str(r))
    ##    while i in range(number):
    ##        print("Spieler "+str(i+1)+" sie sind am Zug")
    ##        if "Spieler is human":
    ##            gc=input("Geben sie eine gewünschten Kartennamen\
    ##               (in der Form [Kartenname,Zahl) ein: ")
    ##            gs=input("Welchen Mitspieler wollen sie fragen? ")
    ##            if "wenn die Gesuchte Karte in der Hand des Gefragten Spielers ist":
    ##                remove "die gesuchte Karte von der Hand des Spielers"
    ##                Spielerhand.append(gc)
    ##            elif gc = 'reset' or gs = 'reset':
    ##                "break"
    ##            elif gc = "End" or gs = "End":
    ##                print("Das Spiel wird nun beendet")
    ##                break
    ##            else:
    ##                print(str(x)+" Ihr zug ist vorbei
    ##        else:
    ##            "Comuputerfunktionen"
    ##    r=r+1

    Quartett_7 = [(Heart,"7"),(Club,"7"),(Spade,"7"),(Diamond,"7")]
    Quartett_8 = [(Heart,"8"),(Club,"8"),(Spade,"8"),(Diamond,"8")]
    Quartett_9 = [(Heart,"9"),(Club,"9"),(Spade,"9"),(Diamond,"9")]
    Quartett_10 = [(Heart,"10"),(Club,"10"),(Spade,"10"),(Diamond,"10")]
    Quartett_Ace = [(Heart,Ace),(Club,Ace),(Spade,Ace),(Diamond,Ace)]
    Quartett_Queen = [(Heart,Queen),(Club,Queen),(Spade,Queen),(Diamond,Queen)]
    Quartett_Jack = [(Heart,Jack),(Club,Jack),(Spade,Jack),(Diamond,Jack)]
    Quartett_King = [(Heart,King),(Club,King),(Spade,King),(Diamond,King)]

