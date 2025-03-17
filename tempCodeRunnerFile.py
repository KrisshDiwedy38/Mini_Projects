
for i in range(5,0,-1):
   result = ' '.join([str(x) for x in range(1,i+1)])
   print(' ' * (6-i) + result)