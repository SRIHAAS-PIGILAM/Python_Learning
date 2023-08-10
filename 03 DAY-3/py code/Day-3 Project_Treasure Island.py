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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice_1 = input('You are at the gate way for the entrance of the game. Where do you want to go? Type "left" or "right\n"').lower()

if choice_1 == "right":
    #continue the game
    print("You choose the correct path....!!")
    choice_2 = input("'Now', you have arrived at the ocean, Do you want to 'swim' or 'wait'......type 'swim' or 'wait'\n ").lower()
    if choice_2 == 'wait':
        #continue the game
        print("You are a calm and cool headed person !!....the help has arrived!!!\n")
        print("Now You are in front of three large doors!!!!....\n")
        choice_3 = input("Now select any one door to find the treasure!!!!....whic door do you want to select...!!???? The 'Red' or 'Yellow' or 'Green..!!??? Select one \n").lower()
        if choice_3 == 'yellow':
            print("Hooooooraaahhhh!!!!.....You win!!!...You found the Treasure!!$$$$")
        elif choice_3 == 'red':
            print("Bad luck you were thrown into sea..!!!!...Game Over..!!")
        else:
            print("Game Over....!!!! You have opened the wrong door and thrown into dark and dangerous forest")
    else:
        print("You were eaten by the sharks and piranas....Game over!...Try again...")

else:
    print("You fell into 'Hell'.... Game Over!")

















