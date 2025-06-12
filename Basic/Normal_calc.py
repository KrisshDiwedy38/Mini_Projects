#Normal calculator

user = str(input("Enter the problem: "))
user.split()
stack = []
for i in user:
   if i.isnumeric():
      stack.append(i)

num2 = int(stack.pop())
num1 = int(stack.pop())
for i in user:
   if i == '+':
      print(num1 + num2)
   elif i == '-':
      print(num1 - num2)
   elif i == '*':
      print(num1  * num2)
   elif i == '/':
      print(num1 / num2)  
   
