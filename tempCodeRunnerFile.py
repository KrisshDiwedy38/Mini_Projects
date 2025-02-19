
repo_name = input("Enter new repository name: ")
description = input("Enter repository description: ")
private_repo = input("Is this a private repository ? (y/n) : ")

if private_repo.lower() == 'n':
   private_repo = False
else:
   private_repo = True

data = { "name" : repo_name , "description" : description , "private" : private_repo}

print(data)
