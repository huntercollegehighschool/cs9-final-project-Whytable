#Use of this page is optional. If you use code here, make sure either import page2 or from page2 import * appear on your main.py page.
#HEAL
# a = health points
# b = demon general kills


def attack(a):
  b = 3
  answerstatus = 1

  while a > 0 and answerstatus ==1 :
    answer = input("What is the square root of 169?: ")
    answer = int(answer)
    if answer == 13:
      answerstatus = 2
      b = b-1
      print("Correct!")
      print("")
      print("You have unlocked another part of the story: ")
      print("After the dramatic question that the man who you found out after was called the King of Mages was posed, you try to make sense of your situation.")
      print("Apparently you're the hero and these strangers that you just met want you to defeat the three Great Demon Generals!")
      print("Well, I guess the only thing you can do it train!")
      print("")
      print("You have ", a, "HP and ", b, "Generals reminaing")
      print("")
    if answer != 13:
      print("Incorrect!")      
      a = int(a - 1)
      print("You have ", a, "HP and ", b, "Generals reminaing")


  while a > 0 and b >= 1 and answerstatus == 2:
    answer = input("What is the sum of 5867 and 1699: ")
    answer = int(answer)
    if answer == 7566:
      answerstatus = 3
      b = b-1
      print("Correct!")
      print("")
      print("After 1 year of gruelling training, you've finally reached the peak skills in order to defeat the Demon Generals.")
      print("You trained with the greatest mage in teh land in order to learn sacred self-healing magic, you trained with the strongest warrior of the land in order to learn how to weild magic swords, and finally, you trained with the strongest martial artist in order to increase all of your physical abilities tenfold!")
      print("Now that you've aquired this power, you can face off against the Demon Generals!")
      print("That is all of the backstory and you are now caught up with the main story.")
      print("")
      print("You have ", a, "HP and ", b, "Generals reminaing")
      print("")
    if answer != 7566:
      print("Incorrect!")
      print("")      
      a = int(a - 1)
      print("You have ", a, "HP and ", b, "Generals reminaing")
      print("")

  while a > 0 and b >= 1 and answerstatus == 3:
    answer = input("If x is equal to 3, what is (49 * x + 13) / 3: ")
    print("")
    answer = int(answer)
    if answer == 50:
      answerstatus = 4
      b = b-1
      print("Correct!")
      print("")
      print("You have ", a, "HP and ", b, "Generals reminaing")
      print("")
    if answer != 50:
      print("Incorrect!")      
      a = int(a - 1)
      print("You have", a, "HP and", b, "Generals reminaing")
      print("")

  if a <= 0:
    a = 0
    return a 

  elif b == 0 and a > 0:
    print("You Win! You beat all of the Generals and you have ", a, "HP remaining.")
    print("The world has finally been saved!")
    print("In the conclusion of events, you ended up defeating the Demon Generals and saving the world! You recieved millions of thanks from the people of this other world and decided to stay.")
    print("")
    a = int(a)
    return a



    