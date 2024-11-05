# zip(*iterables) = aggregate elements from two or more iterables (lists , tupils , sets , etc )
#                   creats a zip object with paired elements stored in tupils for each elements 

username = ("harsh","wheelydos","hewlow") #tupils
passwords = {"123456","heyhello","newpass"} #sets

users = zip(username,passwords) #here users is a zip object
print(type(users))

for i in users:
    print(i)

users = list(users)#changes the type of users object from zip to lists 
print(type(users))
#can be changed into sets ,dict or any ther object type
users = dict(users)
print(type(users))
for key,value in users.items():
    print(key,value)

login_dates = ["5/01", "6/10" ,"20/2"] #list

users_alldata = list(zip(username,passwords,login_dates))

for i in users_alldata:
    print ( i )