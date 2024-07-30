def hello():
    print ("helo")

hello()
print(hello)#this will print the memory adress of hello
hi = hello #this will asign the memory adress of hello to hi 
hi()#this will print the data that was stored in the memory adress of hello 

#another example

say = print
say("hello say told me to print this")