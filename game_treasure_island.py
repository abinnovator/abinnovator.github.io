from colorama import Fore
print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("You are at a crossroads. To the left is a mysterious path, to the right is a dark forest.")
      
choice1 = input('which way do you go left or right?')
choice1.lower()
if choice1 == "left":
  print("You walk down the mysterious path and come to a lake")
  print("You see a big boat with a smaller and less powerful engine with with other people coming and going assuring it is of a good quality in the distance coming from the right which you could use to cross the lake but you also see a bigger but sketchy boat with no protection but with a engine in the left.This bigger boat also does not have manny passengers")
  choice2 = input("which boat do you take left or right?")
  choice2.lower()
  if(choice2 == "right"):
    print("The boat makes it to the island and you see a castle with three doors one red one blue and one yellow")
    choice3 = input("Which door do you choose?")
    choice3.lower()
    if choice3 == "Yellow":
      print("You won the game and found the treasure")
      print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************''')
    elif choice3 == "red":
      print("You fall into a pit of fire and die.")
      print(Fore.RED+'''               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^''')
    else:
      print("You fall into a pit with snakes and die.")
      print(Fore.GREEN+'''                            _.--....
                 _....---;:'::' ^__/
               .' `'`___....---=-'`
              /::' (`
              \'   `:.
               `\::.  ';-"":::-._  {}
            _.--'`\:' .'`-.`'`.' `{I}
         .-' `' .;;`\::.   '. _: {-I}`\
       .'  .:.  `:: _):::  _;' `{=I}.:|
      /.  ::::`":::` ':'.-'`':. {_I}::/
      |:. ':'  :::::  .':'`:. `'|':|:'
    jgs '--.:::...---'\:'.:`':`':./
                       '-::..:::-''')
    
  else:
    print(Fore.GREEN+'''                    .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
          snd                         (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'
''')
    print("The boat is attacked by crocodiles.Game Over")
else:
  print('''
                                                  ,w.
                                                ,YWMMw  ,M  ,
                           _.---.._   __..---._.'MMMMMw,wMWmW,
                      _.-""        """           YP"WMMMMMMMMMb,
                   .-' __.'                   .'     MMMMW^WMMMM;
       _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
    ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
   ,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
   WMMm__,-'.'     /      _.\      F"""-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
   "^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
              /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
             /  .'             /  (       .'  /     Ww._     `.  `"
            /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
   fsc     (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
            `"""                    `"""   `"'                  `---" ''')
  print("You walk into the forest and get eaten by a lion. Game Over")
