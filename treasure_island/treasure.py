print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
      ''')
print("Welcome to Treasure Island.")
print("Your ship sunk and you awakened in an island.")
path = input("Do you wanna walk along the shore or go further inside the island?\nType 'island' or 'shore'\n")
if path.lower() == "island":
    print('''
              _____
              .-" .-. "-.
            _/ '=(0.0)=' \_
          /`   .='|m|'=.   `\
          \________________ /
      .--.__///`'-,__~\\\\~`
     / /6|__\// a (__)-\\\\
     \ \/--`((   ._\   ,)))
     /  \\  ))\  -==-  (O)(
    /    )\((((\   .  /)))))
   /  _.' /  __(`~~~~`)__
  //"\\,-'-"`   `~~~~\\~~`"-.
 //  /`"              `      `\
//
          ''')
    print("You encountered some pirates and were killed\nGame Over.")
elif path.lower() == "shore":
    print('''          |
         \ _ /
       -= (_) =-
         /   \         _\/_
           |           //o\  _\/_
    _____ _ __ __ ____ _ | __/o\\ _
  =-=-_-__=_-= _=_=-=_,-'|"'""-|-,_
   =- _=-=- -_=-=_,-"          |
 jgs =- =- -=.--"
          ''')
    swim = input("You see another small island nearby, do you wanna swim or make a raft?\nType 'swim' or 'raft'\n")
    if swim.lower() == "swim":
        print('''
                        
  _    _,-'    `--,
 ( `-,'            `
  \           ,    o ` 
  /   ,       ;        ` 
 (_,-' \       `, _  ""/
        `-,___ =='__,-'
              ````
              ''')
        print("You were killed by piranhas\nGame Over.")
    elif swim.lower() == "raft":
        print("You managed to get to the island")
        pick = input("You saw an entrance in a strange cave.\nAfter going inside you see 3 paths.\nSelect 'down', 'left' or 'right'\n")
        if pick.lower() == "down":
            print("The cave flooded with water and you drowned. Game Over.")
        elif pick.lower() == "right":
            print("You stepped in a trap and arrows came in your direction from the walls. Game Over")
        elif pick.lower() == "left":
            print("You discovered the treasure chest. You win!")
