list1 = [] #declaring an empty list
print (list1)


list2 = ['Adewumi','Alex','Kayode','Christiana']
print (list2)

list3 = [1,3,5,3,6] #int list
print(list3)

list4 =[1.4,3.5,6.3,5.6] #float list
print(list4)

list5 =[True,False] #Bool list
print(list5)

list6 = [1,2.0, True, 'gbenga'] #heterogenous
print(list6)

#INDEXING
print(list2[0]) #first index +ve indexing
print(list2[-4]) #first index -ve indexing
print(list2[3]) #last index +ve indexing
print(list2[-1]) #last index -ve indexing

list7 = [1,2,3,[4,5,6,[7,8,[9]]],10] #list of list
print(list7)
print(list7[0]) #return 1
print(list7[3]) #returning [4,5,6,7,8,[9]]]
print(list7[4]) #return10
print(list7[3][3]) #returning [7,8,[9]]
print(list7[3][3][2]) #returning 9

#list conversion
list8=[1,2,3,4]
print(type(list8))

list9 = list('sabi programmer') #converting str to list
print(list9)

list10 = list ({1:'one',2:'two'}) #converting a dict to list
print(list10)

list11 = list((10,20,30)) #converting a tuple to list
print(list11)

list12 = list({100,200,300}) #converting set to list
print(list12)
          

#iterate a list
for name in list2:
    print(name)

for ind in range (len(list2)):
    print(list2[ind])

#list operators
print(list2+list3) # +operator
print([1,2,3] * 3) # *operator

print('Adewumi' in list2) #in operator
print('gbenga not in list2') #not operator

print(list2[1:5]) #slicing

#updating list
list2[0] ='vera'
list2.append('michael')
print(list2)

#remove item
print('list2: ', list2)
del list2[0]
print('after del list2[0]: ', list2)

list2.remove('Alex')
print('after removing Alex: ', list2)

print(list2.pop(0)) #remove last index
print('after popping last index: ', list2)

list2.clear() #make the list empty
print(list2)

del list2 #delete list2

#list method
list13 = [2,4,6,8]
#copy function
list14 = list13.copy()
print(list14)

#append function
list13.append(10)
print ('list13: ',list13)
print ('list14: ',list14)

#count function
list13.append(4)
print(list13)
print(list13.count(4))

#entend function
list14.extend([12,14,16])
print(list14)


#index function
print(list14.index(14))
print(list13)
print(list13.index(4))

#insert function
list13.insert(3, 7)#index, value
print(list13)
list13.insert(0,1) #index, value
print(list13)


#pop function
list13.pop(3) #remove at index 3
print(list13)

#remove function
list13.pop() #remove from last index
print(list13)

#reverse function
list13.reverse()
print (list13)

#sort function
list13.sort()
print(list13)
list13.sort(reverse=False)
print(list13)
