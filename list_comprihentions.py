# list comprihentions = a way to creat a new list with less syntax 
#                       can mimic creatain lambda funtions , easier to read 
#                       list = [expression for item in iterable ]                     1
#                       list = [expression for item in iterable if conditional ]      2 
#                       list = [expression if/else for item in iterable ]             3

squares = []
for i in range (1,11):
    squares.append( i*i )
print (squares)
#the above can be written as 

squaresss = [i*i for i in range(1,11)] # 1
print(squaresss)

print("--------------------------------------------------------")

students = [100,90, 20, 30 , 40 , 50 , 60 , 70, 80 ,80]
students_list = list(filter(lambda x :x>=60 , students ))
print (students_list)

#the above can be written as 

studentslist = [i for i in students if i>=60] # 2 
print(studentslist)

studentslist3= [i if i>=60  else "failed" for i in students  ] # 3 
print (studentslist3)

