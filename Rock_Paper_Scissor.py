import random

class user:
   def userChoice():
      print("Choose: rock paper scissor")
      choice = input("> ")
      if choice == "rock" or choice == "scissor" or choice == "paper":
         return choice
      else:
         print("Enter valid input")
         return user.userChoice()

   
class computer:
   def botChoice():
      choices = ["rock", "paper", "scissor"]
      choice = choices[random.randint(0,2)]
      return choice
   
class solution:
   def result(user, bot):
      winner = [
      { 'paper,scissor' : 'scissor'},
      {'paper,rock': 'paper'},
      {'rock,scissor': 'rock'}
      ]
      print(f"user chose {user} and computer chose {bot}")
      if user == bot:
         print("It's a draw")
      else:
         for i in winner:
            if user + "," + bot in i:
               if i[user+','+bot] == user:
                  print("User wins")
               else:
                  print("Computer wins")
            elif bot +  "," + user in i:
               if i[bot+','+user] == user:
                  print("User wins")
               else:
                  print("Computer wins")


def __main__():
   while True:
      userchoice = user.userChoice()
      botchoice = computer.botChoice()
      solution.result(userchoice, botchoice)
      ask = input("Play again (y/n): ")
      if ask == 'n':
         print("Thank you for playing :)")
         break
      elif ask == 'y':
         pass
      else:
         break


__main__()



   


      
