
#  dictionary comprehension = create dictionaries using an expression
#                       can replace for loops and certain lambda functions
#                       dictionary = {key: expression for (key,value) in iterable}                           # 1
#                       dictionary = {key: expression for (key,value) in iterable if conditional}            # 2
#                       dictionary = {key: (if/else) for (key,value) in iterable}                            # 3  
#                       dictionary = {key: function(value) for (key,value) in iterable}                      # 4       

city_temp  = {" mumbai ": 32 ," lucknow ": 42 ," delhi ": 52 ," kashmire ": 12 }
# dictoinary = (key : ((value -32)*(5/9)) for  (kew,values) in city_temp.items())
dictionary = {a : round((b-32)*(5/9)) for (a,b) in city_temp.items() } #The items () method in the dictionary is used to return each item in a dictionary as tuples in a list.
print (dictionary) # 1

print("-----------------------------------------------------------------------------------")

weather = {"kashmir":"cold", "mumbai":"warm","lucknow":"warm","delhi":"warm"}
new_weather  = {key : value for (key,value)in weather.items() if value=="cold" } # 2
print(new_weather)

newer_weather = {key : ("thandi "if value=="cold" else "garmi") for (key,value) in weather.items()  } # 3
print(newer_weather)

new_function = lambda a : "garmi" if a>30 else "thandi"
new_temp = {key : new_function(value) for (key,value) in city_temp.items()}

print(new_temp)