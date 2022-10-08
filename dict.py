dict1={1:"one",2:"two",3:"three"}
print(dict1)
dict2={'i':1, 'ii':2, 'iii':3}
print(dict2)
dict3={(1,2,3): 'ade',(4,5,6) : 'wumi',(7,8,9) : 'sola'}
print(dict3)
dict4={1: ['Nigeria' 'Ghana' 'Brazil'], 2: ['vera','micheal','gbenga']}
print(dict4)
print(type(dict4))
dict5= dict()
print(dict5)
dict6=dict(I="one",II="two",III="three")
print(dict6)
print(dict6['I'])
print(dict6['II'])
print(dict6['III'])


print(dict6.get('I'))
print(dict6.get('Iv'))


for key in dict6:
    print("key="+key, "value="+dict6[key])

dict1["I"]=32
dict1["2"]=40
dict1["3"]=50
print(dict1)

dict1["I"]=4
dict1["II"]=5
print(dict1)

#del
del dict1

dict7={"name":"steve","age":25,"marks":60}
dict8={"name":"Anil","age":23,"marks":75}
dict9={"name":"Asha","age":20,"marks":70}

dict10 = {1:dict7,2:dict8,3:dict9}
print(dict10)
dict11=dict10[1]["age"]
print(dict11)

keys={'mumbai','bangalore','chicargo','new york'}
value = 'çity'
dict12 = dict.fromkeys(keys,value)
print(dict12)

#item
print(dict7.items())
print('after popping(2key):',dict2)
print(dict2.pop(4,'folasade'))
print('popped item:',
dict2.popitem())
dict13={'I':1,'II':3,'V':5}
dict14={'II':2,'V':4}
dict13.update(dict14)
print('updated dictionary:',dict13)
