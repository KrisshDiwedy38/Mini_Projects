arr = [-7, 1, 5, 2, -4, 3, 0] 

for i, value in enumerate(arr):
   totalsum -= value
   if leftsum == totalsum:
      return i
   leftsum += value