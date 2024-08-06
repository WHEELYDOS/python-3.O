#short() method  = used with lists
#short() funtion = used with itterables

students_list = ["ramu","shyamu","monu","montu","sonu"]
students_list.sort()
for i in students_list:
    print(i)

print("------------------------------------------------------------------")
students_iterables = ("ramu","shyamu","monu","montu","sonu")
shorted_iterables = sorted(students_iterables, reverse= True)# reverse = True makes the oder in reverse
for i in shorted_iterables:
    print(i)
print("------------------------------------------------------------------")

students_data = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob","B", 20),
            ("Mr. Krabs","C", 78)]


students_data.sort()
for i in students_data:
    print(i)
print("------------------------------------------------------------------")
grade = lambda grades:grades[1]
students_data.sort(key=grade,reverse = True)
for i in students_data:
    print(i)
print("------------------------------------------------------------------")
age = lambda ages : ages[2] 
students_data.sort(key=age)
for i in students_data:
    print(i)



