__author__ = "5369872: julian raab, 4109208: philipp lang"

from random import randint


Heart="Heart"
Spade="Spade"
Club="Club"
Diamond="Diamond"

Jack="Jack"
Queen="Queen"
King="King"
Ace="Ace"

HeartCards =[(Heart, str(7)),(Heart, str(8)),(Heart, str(9)),\
             (Heart, str(10)),(Heart, Jack),\
             (Heart, Queen),(Heart, King),(Heart, Ace)]
SpadeCards =[(Spade, str(7)),(Spade, str(8)),(Spade, str(9)),\
             (Spade, str(10)),(Spade, Jack),\
             (Spade, Queen),(Spade, King),(Spade, Ace)]
ClubCards =[(Club, str(7)),(Club, str(8)),(Club, str(9)),\
            (Club, str(10)),(Club, Jack),\
            (Club, Queen),(Club, King),(Club, Ace)]
DiamondCards =[(Diamond, str(7)),(Diamond, str(8)),(Diamond, str(9)),\
               (Diamond, str(10)),\
               (Diamond, Jack),\
               (Diamond, Queen),(Diamond, King),(Diamond, Ace)]


global Cards
Cards = []              #Eine Liste mit allen Karten
for i in range(8):
    Cards.append(HeartCards[i])
    Cards.append(SpadeCards[i])
    Cards.append(ClubCards[i])
    Cards.append(DiamondCards[i])

Cards_backup = Cards

##Hashcards = {}          #Erzeugt eine Dictionary mit den Karten
##for i in range(32):     # Habe vergessen warum ich die brauchte ...
##    Hashcards[Cards[i]] = i
##


Quartett_7 = [(Heart, "7"),(Club, "7"),(Spade, "7"),(Diamond, "7")]
Quartett_8 = [(Heart, "8"),(Club, "8"),(Spade, "8"),(Diamond, "8")]
Quartett_9 = [(Heart, "9"),(Club, "9"),(Spade, "9"),(Diamond, "9")]
Quartett_10 = [(Heart, "10"),(Club, "10"),(Spade, "10"),(Diamond, "10")]
Quartett_Ace = [(Heart, Ace),(Club, Ace),(Spade, Ace),(Diamond, Ace)]
Quartett_Queen = [(Heart, Queen),(Club, Queen),(Spade, Queen),(Diamond ,Queen)]
Quartett_Jack = [(Heart, Jack),(Club, Jack),(Spade, Jack),(Diamond, Jack)]
Quartett_King = [(Heart, King),(Club, King),(Spade, King),(Diamond, King)]

global Quartett_list
Quartett_list = [Quartett_7, Quartett_8, Quartett_9, Quartett_10, Quartett_Jack,\
            Quartett_Queen, Quartett_King, Quartett_Ace]








#Eine Funktion um Karten an einen Spieler zu verteilen.
def give_Cards(a:int, b:list, c:list) -> list:
    """ a gibt an wie viele Karten gezogen werden sollen. b ist der Spieler und
    c ist der Stapel, aus dem die Karten gezogen werden."""

    player = b
    cards = c
    for i in range(a):
        z = len(cards)
        x = randint(0,31) % z
        y = cards[x]
        cards.pop(x)
        player[4].append(y)
    return(player)
    return(cards)

    


#Nachfragen einer Karte und gegebenfalls ziehen.
def get_Card(b:list, c:list) -> bool:
 
        x = input("Welche Karte möchtest du ziehen? Nenne die Farbe \
(Hearts, Diamond, Club, Spade): ")
        y = input("Und jetzt den Wert (7 bis Ace): ")
        z = (x, y)

        if z in c[4]:
            b[4].append(z)
            w = c[4].index(z)
            c[4].pop(w)
            return True
        else:
            return False
        


##def new_round(a:None) -> None:
##    a = input()
##    if a == "exit":
##        quartett()
##    else:
##        pass
    



def check_quartett(a:list, c:list) -> list:
    """ Hier wird eine Spielerliste (a) und die Quartettliste (c) eingegeben und
        auf Quartette
        überprüft."""
    
    for i in c:
        b = 0
        for j in i:
            if c[i][j] in a[4]:
                b += 1
                if b == 4:
                    a[3] += 1
                    for k in range(4):
                        u = a[4].index(c[i][k])
                        Cards.append(c[i][k])
                        a[4].pop(u)
                
        




    

#Hier wird eine Spielrunde definiert.
def play_round(a:list) -> list:
    """ Es wird eine Liste mit allen Spielern eingegeben. Darauf wird
       dann eine oder mehrere Runden gespielt. Es kommt dann die veränderte
       Liste wieder zurück."""
    #Die Liste a ist für Spieler gedacht.
    global played_rounds
    played_rounds = 0
    for i in range(len(a)):
        played_rounds += 1
        if Spieler[i][2] == "Human":
            d = input("Von welchem Spieler moechtest du eine Karte ziehen?\
                       (1-" +str(len(a))+"): ")
            if int(d) == i + 1:
                print("Du kannst nicht von dir selbst eine Karte ziehen.\
                       wähle einen anderen Spieler")
                continue
            else:
                get_Card(Spieler[int(d)])
                   
        
            
        
        
    
    
