tpl1=('vera','sola','toyin','gbenga') #str tuple
print(tpl1)
tpl2=(1,2,3,4,5) #int tuple
print(tpl2)
tpl3=(4.0,5.7,6.6,4.5) #float tuple
print(tpl3)
tpl4=(True,False) #boolean tuple
print(tpl4)
tpl5=('vera',2,5.7,True) #heterogenous tuple
tpl6=() #empty tuple
print(tpl6)
tpl7='vera','sola','toyin','gbenga' #str tuple
print(tpl7)
tpl8=1,2,3,4,5 #int tuple
print(tpl8)
tpl9=4.0,5.7,6.6,4.5 #float tuple
print(tpl9)
tpl10=True,False #bool tuple
print(tpl10)
tpl11='vera',2,5.7,True #heterogenous tuple
print(tpl11)

#indexing
print(tpl11[0]) #first index using +ve indexing
print(tpl11[-4]) #first index using -ve indexing

print(tpl11[3]) #last index using +ve indexing
print(tpl11[-1]) #last index using -ve indexing

print(tpl11[1]) #second index using +ve indexing
print(tpl11[-3]) #second index using -ve indexing

#deleting
del tpl10 #delete tpl10

#conversion
tpl12=tuple('Sabi Programmers') #convert str to tuple
print(tpl12)
tpl13=(['Sabi','Programmer']) #convert list to tuple
print(tpl13)
tpl14 =tuple({1,2,3,4,5,6}) #convert set to tuple
print(tpl14)
tpl15 = ({1:'one',2:'two'}) #convert dict to tuple
print(tpl15)

#operators
print(tpl1+tpl3) #+operator
print(tpl4*4) #*operator
print(tpl2[1:3]) #slicing
print(2.4 in tpl13) #in operator
print(2.4 not in tpl13) #not in operator

