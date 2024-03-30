print('''                    _
                   /_'. _
                 _   \ / '-.
                < ``-.;),--'`
                 '--. |__
      /-/-/|o|-|\-\\|\\   / | \
       '`  ` |-|   `` '               |") |_" (_" /"' | | |_" |"\
             |-|                      |"\ |__ ,_) \_, |_| |__ |_/  o  o  o
             |-|O
             |-(\,__
          ...|-|\--,\_....
      ,;;;;;;;;;;;;;;;;;;;;;;;;,.
~~,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')

print("Find the Treasure!")

endQuest = "Game over!"

firstQuest = input("You're at a crossroad, what do you do? turn left or right?").lower()

if firstQuest == "left":
    print("You come across a river!")
    secondQuest = input("Do you swim or wait?").lower()
    if secondQuest == "wait":
        print("You see 3 Doors")
        thirdQuest = input("It's color red, blue, and yellow. Which one you go into?").lower()
        if thirdQuest == "yellow":
            print("You Win! Congratulations!")
        elif thirdQuest == "red":
            print("Burned by Fire!")
            print(endQuest)
        elif thirdQuest == "blue":
            print("Eaten by beasts!")
            print(endQuest)       
        else:
            print(endQuest)     
    else:    
        print("Attacked by Trout")
        print(endQuest)
else:
    print(endQuest)
