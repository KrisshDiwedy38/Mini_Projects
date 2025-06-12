number = int(input("Enter any number: "))
reversed_num = 0
temp = number
while number != 0:
  digit = number % 10
  reversed_num = reversed_num * 10 + digit
  number //= 10

if temp == reversed_num:
  print(f"{temp} is a palidrome")
else:
  print(f"{temp} is not a palidrome")