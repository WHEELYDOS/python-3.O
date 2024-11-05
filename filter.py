#filter() = creates a collection of elements from iterables for wich a funtion returns 
#
#filter(funtions , iterables)


data = (("person 1 ", 34),
        ("person 2 ", 25),
        ("person 3 ", 17),
        ("person 4 ", 18))
new_data = lambda info : info[1]>=18 #if age is lower tahn 18 it wil not print that person
lists = list(filter(new_data,data))
for i in lists:
    print(i)