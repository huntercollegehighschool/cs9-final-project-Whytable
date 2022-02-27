"""
Name(s): Navin Gilchrist
Name of Project: The Hero's Quest
"""

#Write the main part of your program here. Use of the other pages is optional.

import os

#Set all game variables

def main():

  name = input("Enter your name: ")
  print("")
  print("Thank you " + name + "!")

  print("As you opened your eyes, everything was bright.")
  print("Who were you? Where were you? Why couldn't you remember anything?!")
  print("As your vision became clearer, you realized that")
  print("you were sitting on what looked like a magic circle.")
  print("Suddenly memories flashed through your mind! You remember walking home ")
  print("from school and sundennly a glowing light emerged from the ground.")
  print("You panicked and tried to run from it but your feet were planted to the ground.")
  print("You realized that the glow on the ground looked like a")
  print("magic circle from the fantasy RPG games you played.")
  print("After that, you blacked out.")
  print("After remembering what happend, you look around and ")
  print("see multiple people dressed in funny looking clothes holding large staffs.")
  print("They all started to celebrate and raised their hands")
  print("in celebration while you sat on the floor, confused.")
  print("You muster up the courage to speak,")
  print("'Umm...excuse me? What's going on? Also where am I, ")
  print("and who are you?' Everyone looked back at you.")
  print("As you made out their faces, you could tell that they ")
  print("looked human. After breathing a sigh of relief, you stood up and confidently spoke: ")
  print("'Please answer my questions. I do not know what is going on")
  print("and I do not know who you are!'")
  print("One of the 7 people in the bunch stepped foreward.")
  print("'Hello hero. You have been summoned to our world")
  print("because we humans are on the brink of extinction!")
  print("As per the prophecy that we have read in our ancient texts,")
  print("following spell in order to summon a hero from another world.")
  print(" This hero should be trained as soon as possible which will")
  print("activate his ability to defeat any foe.- Please help save us from the demons hero!'")
 
  print("As you defeat each Demon General, you will unlock a bit of the story, so please try your best!")
  print("")
  
  # Initial Variables  

  HP = 3
  HP = int(HP)
  #Health of the character

  Healcount = 0
  #Number of times character has healed

  Healcountmax = 3
  #Maximum number of times character can heal

  GameChoice = input("Enter '1' to attack or '2' to heal yourself: ")
  print("")
  # set Game Status to track when player Wins
  Gamestatus = 1

  while GameChoice not in ['1', '2']:
    os.system('clear')
    print("That's not a valid input.")
    GameChoice = input("Enter '1' to attack or '2' to heal yourself: ")
    print("")

  #os.system('clear')
  GameChoice = int(GameChoice)   

  while GameChoice == 2 and HP <7 and HP >0 and Healcount < Healcountmax and Gamestatus == 1:
    from page1 import heal
    HP = heal(HP)
    Healcount = Healcount + 1 
    print("You have successfully increased your Health Points to: ",HP)
    print("You have", Healcountmax - Healcount, "more heal spells you can cast!")
    GameChoice = input("Enter '1' to attack or '2' to heal yourself: ")
    GameChoice = int(GameChoice)
    print("")

  while GameChoice == 2 and HP <7 and HP >0 and Healcount == Healcountmax and Gamestatus == 1:
    print("You do not have enough mana to heal yourself!")
    GameChoice = input("Enter '1' to attack or '2' to heal yourself: ")
    GameChoice = int(GameChoice)
    print("")

  while GameChoice == 1 and HP > 0 and Gamestatus == 1:
    from page2 import attack
    print("You will begin your conquest against the 3 Demon Generals!")
    print("Each correct answer to the question prompt results in a single General eliminated.")
    print("Each Incorrect answer to the question prompt results in a loss of 1 HP.")
    print("You will also start with 3 HP which can be increase to up to 6 HP using 'heal'.")
    print("You must answer three mathematical questions correctly (one for each enemy) and still have more than 0 HP to advance to the battle with the Demon Lord")
    print("Good luck")
    print("")

    HP = attack(HP)
    #HP = int(HP)
    print("You have", HP, "Health points remaining")
    print("")
#    GameChoice = input("Enter '1' to attack or '2' to heal yourself: ")  
#    GameChoice = int(GameChoice)   
#    if GameChoice in ['1', '2'] and HP <= 0: 
#      print("You no longer have enough HP to fight! End of Game")
    if HP == 0:
      print("You've run out of health! GAME OVER.")
    else:
      #sets  Game status to 0 to end game
      Gamestatus = 0
      print("Thank you for playing", name)
      print("Congratulations on defeating the Demon Generals!")
#  while GameChoice == 1 and HP <1 and Healcount <= Healcountmax:
#    print("You should heal yourself and try again.")
#    print("You have", HP, "Health points remaining")
#    GameChoice = input("Enter '1' to attack or '2' to heal yourself: ")  


if __name__ == '__main__':
  main()


