str1= 'my name is Gbenga' # assigning a single qoute
print(str1)
str2="my name is Gbenga" # assigning double quote
print(str2)
str3='''my name is Gbenga''' # assigning tripple quote
print(str3)
str4="""my name is Gbenga"""
print(str4)

#MULTIPLE STRING
str5='''this is my
own multiple-line string
using single quote
'''#assigning triple single quote multiple=line string
print (str5)
str6 = """this is mt
second multiple-line string
using double quote """ #assigning triple double quote
print(str6)
str7 ='welcome to "Gbenga s" class' #including double quote in single quote
ptint(str7)
str8 = "welcome to Gbenga's class" #including single quote in single string
print(str8)

# String length and indexing
str9 = 'Sabi Programmer'
print(len(str9)) # return the length of str9

print(str9[0]) #return first index using +ve indexing
print(str9[-15]) #return last index using -ve indexing

print(str9[14]) #return the 8th index using +ve indexing
ptint(str9[-7]) #return 8th index using -ve indexing


#ESCAPE SEQUENCES
str10 = 'welcome to \'Gbenga s'\ class' #escape sequence in single quote
print(str10)

str11 = "welcome to \"Gbenga s"\ class" #escape sequence in double quote
print(str11)

str12 = r'welcome to \'Gbenga s'\ class'
 #ignoring sequence using escape s

str13 = 'http:\\sabiprogrammers.com\\home' #escape sequence to include back slash
print(str13)

str14 ='Including\tDistance' #include tab in a string
print(str14)

str15 ='Go to \nNext line' #include newline
print(str15)

#STRING OPERATORS
str16 = 'catherine'
str17 = 'welcome back'
print(str16+str17) # concatenating two strings
print(str16*3) #kate how many times would i call you
print(str16[0:4]) # slicing
print(str16[5:9]) # slicing
print('kate' in str16) #check if kate is in str16
print('back' in str17)#is back in str17
print('kate' not str16) #check if kate is not in str16
print('come' not in str17) #is come not in str17

