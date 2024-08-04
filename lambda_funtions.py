# lambda funtions = funtions written in one line using lambda keyword
#                   accepts any number of argument,but only has one expression
#                   (think of it as a shortcut)
#                   (usefull if needed for a short period of time , throw away)

# lambda parameters : expressions

def double(x):
    return x*2

print (double(2))

 # if we will write this funtion in lambda language then we will wite it as 
 # lambda x : x*2

Double = lambda x : x*2
print(Double(2))

multiply = lambda x,y : x*y
print(multiply(3,4))

add = lambda x,y,z : x+y+z 
print(add(2,4,6))

full_name = lambda a ,b,c : a+" "+b +" "+c
print(full_name("harsh","vardhan","sahu" ))

age_check= lambda age : True if age<18 else False
print(age_check(12))
