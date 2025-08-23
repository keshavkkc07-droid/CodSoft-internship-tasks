import random

print("WELCOME TO MY GAME STONE PAPER SCISSORS")


print("\n")
score=0

def playgame():
  global score

  print(score)
  option=input("choose among stone , paper or scissors :").lower()
  print("\n")


  value=random.randint(1,3)

  if option=="stone":
    if value ==1:
      print("Tie")
      print("Your score is : ",score)

    elif value==2:
      print("soory you loose 🫣🫣")
      score=0
      print("Your score is : ",score)
    elif value==3:
      print("YEH you won 😎😍🥳🥳🎊👯‍♂️")
      score+=5
      print("Your score is : ",score)
  


  elif option=="paper":
    if value ==2:
      print("Tie")
    elif value==3:

      score=0
      print("Your score is : ",score)
      print("soory you loose 🫣🫣")


    elif value==1:
      print("YEH you won 😎😍🥳🥳🎊👯‍♂️")
      print("YEH you won 😎😍🥳🥳🎊👯‍♂️")
      score+=5
      print("Your score is : ",score)
  

  

  elif option=="scissors":
    if value ==3:
      print("Tie")
      print("Your score is : ",score)

    elif value==1:
      print("soory you loose 🫣🫣")

      score=0
      print("Your score is : ",score)

    elif value==2:
      print("YEH you won 😎😍🥳🥳🎊👯‍♂️")
      print("YEH you won 😎😍🥳🥳🎊👯‍♂️")
      score+=5
      print("Your score is : ",score)
  

    
  else :
    print("SOORY INVALID INPUT")
    
  print("\n")
  print(f"You choose {option}")

  if value==1:
    print("computer choosed STONE")
  elif value==2:
    print("computer choose PAPER")
  elif value==3:
    print("computer choosed scissors")

playgame()
def restart():
  x=input("To restart game Enter 1 : ")
  if x=="1":
    playgame()
    restart()
  else:
    print("exiting....")

restart()