# high order functions = a funtion that either :
#                           1. accepts a funtion as an argument
#                                            or 
#                           2. returns a funtion 
#                           (in python  funtions are also treated as objects )

def divisor(x):
    def dividant(y):
        return y / x
    return dividant

divide = divisor(2)
print(divide(6))

def sqrt(x):
    def process(y):
        return x/y
    return process
sqrrt = sqrt(25)
print(sqrrt(5))