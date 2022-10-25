def greet(name):  
    print ('Hello ', name)

greet('Steve') # calling function with argument
greet(123)

#
def greet(name1, name2, name3):  
    print ('Hello ', name1, ' , ', name2 , ', and ', name3)

greet('Steve', 'Bill', 'Yash') # calling function with string argument

#
def greet(*names):
	i=0
	print('Hello ', end='')
	while len(names) > i:
		print(names[i], end=', ')
		i+=1

greet('Steve', 'Bill', 'Yash') 
greet('Steve', 'Bill', 'Yash', 'Kapil', 'John', 'Amir')

#
def greet(firstname, lastname):
    print ('Hello', firstname, lastname)

greet(lastname='Jobs', firstname='Steve') # passing parameters in any order using keyword argument


#
def greet(name = 'Guest'):
    print ('Hello', name)

greet()
greet('Steve')

#
def sum(a, b): 
    return a + b

#
total=sum(10, 20) 
print(total)
total=sum(5, sum(10, 20))
print(total)



#
def greet(**person):
	print('Hello ', person['firstname'],  person['lastname'])

greet(firstname='Steve', lastname='Jobs')
greet(lastname='Jobs', firstname='Steve')
greet(firstname='Bill', lastname='Gates', age=55) 
greet(firstname='Bill') # raises KeyError




