__author__ = "5369872: julian raab, 4109208: philipp lang"

from random import randint

import os
if os.name == "posix":
    os.system('clear')
elif os.name in ("nt", "dos", "ce"):
    os.system('cls')
else:
    print(80*'\r\n')






Hearts = "Hearts"
Spades = "Spades"
Clubs = "Clubs"
Diamonds ="Diamonds"

Jack = "Jack"
Queen = "Queen"
King = "King"
Ace = "Ace"

HeartsCards = [(Hearts, str(7)),(Hearts, str(8)),(Hearts, str(9)),\
             (Hearts, str(10)),(Hearts, Jack),\
             (Hearts, Queen),(Hearts, King),(Hearts, Ace)]
SpadesCards = [(Spades, str(7)),(Spades, str(8)),(Spades, str(9)),\
             (Spades, str(10)),(Spades, Jack),\
             (Spades, Queen),(Spades, King),(Spades, Ace)]
ClubsCards = [(Clubs, str(7)),(Clubs, str(8)),(Clubs, str(9)),\
            (Clubs, str(10)),(Clubs, Jack),\
            (Clubs, Queen),(Clubs, King),(Clubs, Ace)]
DiamondsCards = [(Diamonds, str(7)),(Diamonds, str(8)),(Diamonds, str(9)),\
               (Diamonds, str(10)),\
               (Diamonds, Jack),\
               (Diamonds, Queen),(Diamonds, King),(Diamonds, Ace)]


global Cards
Cards = []              #Eine Liste mit allen Karten
for i in range(8):
    Cards.append(HeartsCards[i])
    Cards.append(SpadesCards[i])
    Cards.append(ClubsCards[i])
    Cards.append(DiamondsCards[i])

Cards_backup = Cards

##Hashcards = {}          #Erzeugt eine Dictionary mit den Karten
##for i in range(32):     # Habe vergessen warum ich die brauchte ...
##    Hashcards[Cards[i]] = i
##


Quartett_7 = [(Hearts, "7"),(Clubs, "7"),(Spades, "7"),(Diamonds, "7")]
Quartett_8 = [(Hearts, "8"),(Clubs, "8"),(Spades, "8"),(Diamonds, "8")]
Quartett_9 = [(Hearts, "9"),(Clubs, "9"),(Spades, "9"),(Diamonds, "9")]
Quartett_10 = [(Hearts, "10"),(Clubs, "10"),(Spades, "10"),(Diamonds, "10")]
Quartett_Ace = [(Hearts, Ace),(Clubs, Ace),(Spades, Ace),(Diamonds, Ace)]
Quartett_Queen = [(Hearts, Queen),(Clubs, Queen),(Spades, Queen),(Diamonds ,Queen)]
Quartett_Jack = [(Hearts, Jack),(Clubs, Jack),(Spades, Jack),(Diamonds, Jack)]
Quartett_King = [(Hearts, King),(Clubs, King),(Spades, King),(Diamonds, King)]

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
    """Erster Wert ist die Spielerliste, die eine Karte erhaelt.
       Der zweite Wert ist die Spielerliste, von der gezogen wird.
    """
    #Eingabe (Player[i], Player[j])
    x = input("Welche Karte möchtest du ziehen? Nenne die Farbe \
(Hearts, Diamonds, Clubs, Spades). Bedingung ist, \
du musst den Wert schon auf deiner Hand halten: ")
    y = input("Und jetzt den Wert (7 bis Ace): ")
    z = (x, y)
    u = 0
    
    for i in b[4]:
        if y != i[1]:
            u += 1
            if u == len(b[4]):
                print("Du darfst nur Kartenwerte, die du auf der Hand \
hast, ziehen!")
                return False

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
    



def check_quartett(a:list, c:list) -> bool:
    """ Hier wird eine Spielerliste (a) und die Quartettliste (c) eingegeben und
        auf Quartette
        überprüft."""
    
    for i in c:
        b = 0
        v = []
        for j in i:
            if j in a[4]:
                b += 1
                v.append(j)
            if b == 4:
                a[3] += 1
                for k in range(4):
                    u = a[4].index(v[0])
                    Cards.append(v[0])
                    a[4].pop(u)
                    v.pop(0)
                    return True
                    
                
        




    

#Hier wird eine Spielrunde definiert.
def play_round(a:list) -> None:
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
                   




        
            
#Überprüft auf Handkarten       
def check_player(a:list) -> bool:
    """Gebe die Liste Player (a) ein. Die Funktion prüft die Handkarten."""
    b = 0
    for i in a:
        if len(i[4]) == 0:
            b += 1
    if b == 0:
        return True
    else:
        return False















        
    
    
