__author__ = "5369872: julian raab, 4109208: philipp lang"

import implementierung


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

for i in range(number):
    print(Spieler[i])

if(Spieler<3):
    Spieler_1=Spieler.index[0]
    Spieler_2=Spieler.index[1]
    
    Spieler_1.append()
    Spieler_2.append()

    Stapel = []
    Stapel.append()
else:
   while i in range(lenght(Spieler)):
       Spieler_i=Spieler.index[i]
       Spieler_i.append()
       
   



Quartett_7 = [(Heart,7),(Club,7),(Spade,7),(Diamond,7)]
Quartett_8 = [(Heart,8),(Club,8),(Spade,8),(Diamond,8)]
Quartett_9 = [(Heart,9),(Club,9),(Spade,9),(Diamond,9)]
Quartett_10 = [(Heart,10),(Club,10),(Spade,10),(Diamond,10)]
Quartett_Ace = [(Heart,Ace),(Club,Ace),(Spade,Ace),(Diamond,Ace)]
Quartett_Queen = [(Heart,Queen),(Club,Queen),(Spade,Queen),(Diamond,Queen)]
Quartett_Jack = [(Heart,Jack),(Club,Jack),(Spade,Jack),(Diamond,Jack)]
Quartett_King = [(Heart,King),(Club,King),(Spade,King),(Diamond,King)]

