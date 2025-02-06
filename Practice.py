class Dog:
   dogs = []

   def __init__(self, name):
      self.name = name
      self.dogs.append(name)

   @classmethod
   def print_objects(self):
      return self.dogs


dog1 = Dog("Whiskey")
dog2 = Dog("Franklin")
dog3 = Dog("Cookie")

print(dog2.print_objects())