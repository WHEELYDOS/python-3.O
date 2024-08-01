# high order functions = a funtion that either :
#                           1. accepts a funtion as an argument
#                                            or 
#                           2. returns a funtion 
#                           (in python  funtions are also treated as objects )

def loud (text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(funtion):
    text = funtion("helo")
    print(text)
    print(text:=funtion("hello")) #this i a example of walrush operator in python 2.O
hello (loud)
hello(quiet)