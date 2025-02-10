def game_cont(myfunc):
   while True:
      myfunc()
      ask = input("Play again (y/n): ")
      if ask == 'n':
         print("Thank you for playing :)")
         break
      elif ask == 'y':
         pass
      else:
         break

