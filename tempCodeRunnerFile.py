import random
number = random.randint(0,100)

while True:
   ask_user = int(input("Guess: "))
   if number == ask_user:
      print("You got it!")
      break
   elif ask_user > number:
      print("Too high")
   elif ask_user < number:
      print("Too low")
   else:
      continue
