# for loop practice

# print to 0 to (n-1)=10-1=9
for i in range(10):
   print("printed number: ",i)


# print 1 to 9 : all even number will print
for i in range(1,10,2):
   print(f"Even numbers:{i}")

# start will 3, and increase 4 by 4 and till 19. <20
for i in range(3,20,4):
   print(i)

for i in range(0,10):
   if(i==3): 
      break
   print(i)
print("reached end")


# while loop practice

i=1
while i<6:
   print(i)
   i=i+2

n=int(input(f"enter your in value: "))
if n>20 or n==-1:
   print("please, enter valid number")
   exit()
while n<20:
   print(n)
   n=n+4
   if(n==5):
      break


