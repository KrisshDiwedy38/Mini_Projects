num = [ 2,7,3,8,1,4]
count = 0

def swap( num, a , b):
   num[a],num[b] = num[b],num[a]

while num != sorted(num):
   for i in range(0,len(num)-1):
      if num[i] > num[i+1]:
         swap(num,i,i+1)
         count += 1

print(num)
print(count)
