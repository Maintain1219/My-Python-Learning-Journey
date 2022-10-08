set1 ={1,2,3,4,5} #int set
print(set1)

set2 ={1.0,2.1,3.2,4.3} # float se
print(set2)

set3 ={'1','2','3','4'} #str set
print(set3)

set4 ={True,False,True,False}#boolean set
print(set4)

set5 ={1,2.1,False,'3'}#heterogenous set
print(set5)

set6=() #empty set
print(set6)
print(type(set6))

set7 = {(12,57,43), 1,2.4,"great"} #set of hashable
print(set7)

#conversion
set8 = set('Sabi Programmers')#converting str to set
print (set)


set9 =(['Sabi', 'Programmers'])#converting list to set\
print (set9)

set10 = (('Sabi', 'Programmers')) #converting tuple to set
print(set10)


set11 = set({1:'Sabi',2:'Programmers'}) #converting dict to set
print(set11)

#set methods
set12=set()
#add
set12.add(20)
set12.add('Christiana')
set12.add(True)
set12.add(40.123)
print('set 12: ',set12)


#Updatin method
set13={'Vera', 'Alex', "sola", 'wumi'}
set12.update(set13)
print('set13: ',set13)
print('set 12 after updating: ',set12)

#or operator
set14={1,2,3,4,5}
set15={4,5,6,7,8}
print(set14|set15, "using |")
print(set14 or set15, "using or")

#and operator
print(set14&set15, "using &")
print(set14 and set15, "using and")


#-operator
print(set14-set15, "using set14-set15")
print(set15-set14, "using set15-set14")

#^ operator
print(set14^set15, "using^")

#union method
print(set14.union(set15), "using union")


#intersection
print(set14.intersection(set15), 'using intersection')

#difference
print(set14.difference(set15), 'using difference')

#symmetric difference
print(set14.symmetric_difference(set15), 'using symmetric difference')

#copy method
set16=set3.copy()
print(set16)

#difference update
set14={1,2,3,4,5}
set15={4,5,6,7,8}
print('set14 before difference update: ',set14)
print('set15 before difference update: ',set15)
set14.difference_update(set15)
print('set14 after difference update: ',set14)
print('set15 after difference update: ',set15)

#intersection update
set14={1,2,3,4,5}
set15={4,5,6,7,8}
print('set14 before intersection update: ',set14)
print('set15 before intersection update: ',set15)
set14.intersection_update(set14)
print('set14 after intersection update: ',set14)
print('set15 after intersection update: ',set15)

#symmetric_difference update

set14={1,2,3,4,5,6}
set15={4,5,6,7,8}
print('set14 before symmetric_difference update: ',set14)
print('set15 before symmetric_difference update: ',set15)
set14.symmetric_difference_update(set15)
print('set14 after symmetric_difference update: ',set14)
print('set15 after symmetric_difference update update: ',set15)

#discard method
set14={1,2,3,4,5,6}
set15={4,5,6,7,8}
print(set14.discard(4))

#remove method
set14={1,2,3,4,5,6}
set15={4,5,6,7,8}
print(set15.remove(6))

#issubset method
set17={1,2}
print(set17.issubset(set14))

#isdisjoint method
set18={20,30}
print(set18.isdisjoint(set14))

#pop method
set16 = {1,2,3,4,5,6}
print('pooped value: ', set16.pop())
print('new set16: ', set16)
