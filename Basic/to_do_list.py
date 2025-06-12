#TO DO LIST 

toDo = {}

def toDo(choice):
   if choice == '1':
         task = input("Enter a task: ")
         toDo[task] = 'Not Done'
      
   elif choice == '2':
      count = 1
      for i in toDo:
         print(f"{count}. {i} : {toDo[i]}")
         count +=1
   
   elif choice == '3':
      delete =  int(input("Enter task number to be deleted: "))
      for i in range(len(toDo)):
         if delete == i+1:
            del  toDo[list(toDo.keys())[i]]
            print(f"Task {delete} has been deleted")
         else:
            print("Invalid task number")

   elif choice == '4':
      update = int(input("Enter task number to be updated: "))
      if 1 <= update <= len(toDo):
         toDo[list(toDo.keys())[update-1]] = "Done"
      else:
         print(f"Task number - {update} is not in the list")


   elif  choice == '5':
      print("Thank you for using the to-do list")
      print("Goodbye!")
      exit()

   else:
      print("Invalid choice. Please choose a valid option")
      __main__()

def __main__():
   while True:
      print("Add Task - Press 1")
      print("View Task - Press 2")
      print("Delete Tasks - Press 3")
      print("Change Status -  Press 4")
      print("Exit - Press 5")
      user = input("Enter your choice: ")
      if user == '5':
         break
      else:
         ask =  input("Do you want to continue? (yes/no): ")
         if  ask.lower() == 'no':
            print("Thank you for using the to-do list")
            print("Goodbye!")
            break
         else:
            __main__()



__main__()
   