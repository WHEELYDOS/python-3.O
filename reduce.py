# reduce () = apply a funtion to a iterable and reduce it to a single cumulative value .
#             performs funtion on first two element and repeats process until 1 value
#             remains

# reduce ( function , iterables ) 
 
import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x,y : x+y , letters)# makes word ["HE","L","L","O"] then ["HEL","L","O"] till it becomes "HELLO"
print (word)

factorial =[5,4,3,2,1]
numbers = functools.reduce(lambda x,y :x*y , factorial)
print (numbers)