import random
from Pre_def_funcs import game_cont
   
def sktech(num):
   pos1 ="""

   _______
   |    |
   |    
   |  
   |  
   |
   """

   pos2 =  """

   _______
   |    |
   |    O
   |  
   |   
   |
   """
   pos3 = """

   _______
   |    |
   |    O
   |    | 
   |   
   |
   """
   pos4 = """

   _______
   |    |
   |    O
   |    | \\
   |   
   |
   """
   pos5 = """

   _______
   |    |
   |    O
   |  / | \\
   |   
   |
   """
   pos6 = """

   _______
   |    |
   |    O
   |  / | \\
   |   / 
   |
   """
   pos7 = """

   _______
   |    |
   |    O
   |  / | \\
   |   / \ 
   |
   """
   figures = [pos7,pos6,pos5,pos4,pos3,pos2,pos1]
   return figures[num]

def word_output(word, guessed_letters):
   return ''.join([letter if letter in guessed_letters else '_' for letter in word])


def Hangman():
   words = [
    "apple",
    "giraffe",
    "laptop",
    "mountain",
    "puzzle",
    "sapphire",
    "kangaroo",
    "whistle",
    "dolphin",
    "volcano",
    "zebra",
    "rainbow",
    "python",
    "galaxy",
    "island",
    "cactus",
    "elephant",
    "castle",
    "horizon",
    "forest"
   ]  

   word_to_guess = random.choice(words)
   word_length = len(word_to_guess)
   guessed_letters = []
   wrong_guesses = 6

   print("Welcome to Hangman!\n")
   print(f"The word to be guess is of {word_length} letters")

   while wrong_guesses > 0:
      print(f"Wrong Guesses left: {wrong_guesses}")
      print(f"Guessed Letters: {guessed_letters}")
      current_state = word_output(word_to_guess, guessed_letters)  
      print(f"Current State: {current_state}")
      print(sktech(wrong_guesses))

      if current_state == word_to_guess:
         print("You have guess all the letters, GOOD JOB!")
         break
      
      guess = input("Guess-> ").lower()

      if not guess.isalpha() or len(guess) != 1:
         print("Invalid input!")
         continue

      if guess in guessed_letters:
         print(f"You have already guesssed this word! Try another")
         continue
      
      guessed_letters.append(guess)

      if guess in word_to_guess:
         print(f"{guess} is present in the word!")
         continue
         
      else:
         print(f"Wrong Guess!")
         wrong_guesses -= 1
         continue
         

   else: 
      print("\nGame over! You've run out of attempts.")
      print(sktech(wrong_guesses))
      print(f"The word was: {word_to_guess}")



game_cont(Hangman)

