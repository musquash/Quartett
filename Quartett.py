__author__ = "5369872: julian raab, 4109208: philipp lang"

from implementierung import *
#import sys

def quartett():
    """Die Funktion startet ein Spiel
       """



#########################################################################
    #Ab hier werden die Spieler erzeugt.
    while True:
        number = int(input("Anzahl der Spieler bitte eintragen (2-8): "))

        if number > 8 and number != 999:
                print("FEHLER zu viele Spieler")
        elif number < 2:
            print("FEHLER zu wenig Spieler")
        elif number == 999:
            quartett()
        else:
            print("Okay sie haben nun " + str(number) +" Mitspieler")
            break

        
    global Player
    Player = []
    #Diese Liste beinhaltelt alle Spieler mit deren Informationen
    #Also Player = [[Player 1], [Player 2], ...]
    #Die Elemente [Player x] sind ebenfalls Listen:
    #[Player x] = [Nummer, Name, Status, Punkte, [Handkarten]]
    
    #Nummer = Nummer der Spieler von minimal 2 - 8 Spieler
    
    #Name = Name des Spielers bzw. dessen Bezeichnung
    
    #Status = ob es sich um einen Menschen oder einen Computer handelt
    
    #Punkte definiert, die bereits abgelegten Quartette
    
    #Die Liste Handkarten zeigt welche Karten der Spieler auf der "Hand" hat,
    #d.h. welche Karten er Nachfragen lassen kann 


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
       Player.append(xliste)



       
    #Verteilung der Karten auf die Spieler (nach Spieleranzahl).
    if(number < 3):
##        Spieler_1 = Spieler[0]
##        Spieler_2 = Spieler[1]

        give_Cards(10, Player[0], Cards)
        give_Cards(10, Player[1], Cards)

        Stapel = Cards
    else:
        r = len(Cards) % number
        t = int(len(Cards) / number)
        for i in range(number):
            give_Cards(t, Player[i], Cards)
        if r > 0:
            for i in range(r):
                Player[i][4].append(Cards[0])
                Cards.pop(0)
                
            
# Hier ist die Erstellung der Spieler beendet.
#########################################################################


 

    for i in range(number):
        print(Player[i])


#Beginn einer Runde
    p = randint(0, number - 1)
    while True:
        if check_player(Player) == True:
            print("Es spielt nun Spieler {:}.".format(p + 1))
            print("Deine Handkarten:", Player[p][4])
            print("Deine bisherigen Quartette: ", Player[p][3])
            g = input("Suche dir einen Spieler aus, von dem du eine \
Karte ziehen willst. (1 bis {:}) ".format(number))
            while True:
                if g == (p - 1):
                    print("Du kannst nicht von dir selbst eine Karte ziehen!")
                else:
                    if get_Card(Player[p], Player[int(g) - 1]) == True:
                        print("Du hast erfolgreich eine Karte gezogen.")
                        print("Deine Handkarten:", Player[p][4])
                        print("Du darfst weiter ziehen.")
                        check_player(Player)
                        #p += 1 % number
                    else:                   
                        print("Die Karte war leider nicht vorhanden. Der \
nächste Spieler ist dran.")
                        b = input("Drücke eine beliebige Taste zum fortsetzen.")
                        p = (p + 1) % number
                        break
    
        else:
            return False

                    
                    
                
                
            
        
        
        




































   
    ##while go_on=Ture
    ##    if eingabe=reset:
    ##        go_on=False
    ##        continue
    ##    else:
    ##        for 'Handkarten_oder_so' > 0:
    ##            print("Runde "+str(r))
    ##            while i in range(number):
    ##                print("Spieler "+str(i+1)+" sie sind am Zug")
    ##                if "Spieler is human":
    ##                    gc=input("Geben sie eine gewünschten Kartennamen\
    ##                    in der Form [Kartenname,Zahl) ein: ")
    ##                    gs=input("Welchen Mitspieler wollen sie fragen? ")
    ##                    if "wenn die Gesuchte Karte in der Hand des\
    ##                     Gefragten Spielers ist":
    ##                        remove "die gesuchte Karte von der Hand des Spielers"
    ##                        Spielerhand.append(gc)
    ##                    elif gc = "End" or gs = "End":           )
    ##                        print("Das Spiel wird nun beendet")  --> irgendwie ab ändern
    ##                        sys.exit(0)                          )
    ##                    else:
    ##                        print(str(x)+" Ihr zug ist vorbei")
    ##                else:
    ##                    "Comuputerfunktionen"
  

##    Quartett_7 = [(Heart,"7"),(Club,"7"),(Spade,"7"),(Diamond,"7")]
##    Quartett_8 = [(Heart,"8"),(Club,"8"),(Spade,"8"),(Diamond,"8")]
##    Quartett_9 = [(Heart,"9"),(Club,"9"),(Spade,"9"),(Diamond,"9")]
##    Quartett_10 = [(Heart,"10"),(Club,"10"),(Spade,"10"),(Diamond,"10")]
##    Quartett_Ace = [(Heart,Ace),(Club,Ace),(Spade,Ace),(Diamond,Ace)]
##    Quartett_Queen = [(Heart,Queen),(Club,Queen),(Spade,Queen),(Diamond,Queen)]
##    Quartett_Jack = [(Heart,Jack),(Club,Jack),(Spade,Jack),(Diamond,Jack)]
##    Quartett_King = [(Heart,King),(Club,King),(Spade,King),(Diamond,King)]
##
