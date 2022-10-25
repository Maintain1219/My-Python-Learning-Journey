nums = [10, 20, 30, 40, 50] #list object

for i in nums:
    print(i)

nums = (10, 20, 30, 40, 50) #tuple object
for i in nums:
    print(i)

for char in 'Hello':  #string statement
    print (char)

numNames = { 1:'One', 2: 'Two', 3: 'Three'} #dict loop

for pair in numNames.items():
    print(pair)


numNames = { 1:'One', 2: 'Two', 3: 'Three'} #key and value dict loop

for k,v in numNames.items():
    print("key = ", k , ", value =", v)

for i in range(5):  #for loop in range
    print(i)

for i in range(1, 5): #for loop can be stop or exit using break
    if i > 2:
        break
    print(i)

for i in range(1, 5): #for loop Continue Next Iteration
    if i > 3:
        continue
    print(i)

for i in range(2): #For Loop with Else Block
    print(i)
else:
     print('End of for loop')

for x in range(1,4):  #Nested for Loop
    for y in range(1,3):
        print('x = ', x, ', y = ', y) 
