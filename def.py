def dosomething(fn):
	    print('Calling function argument:')
	    fn()
dosomething(lambda : print('Hello World'))
myfn = lambda : print('Hello World') 
dosomething(myfn) # passing lambda function
