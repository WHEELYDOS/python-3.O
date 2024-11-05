import time
#epoch = a date and time from which a computer measures time 
print(time.ctime(0))# converts a time expressed in seconds since epoch to a reasonable string 
                    #0 is measured in seconds
                     # the time is measured in seconds
print (time.time())#prints the second that has passed since the epoch

print(time.ctime(time.time()))#thiss will print the curent date and time


time_obj = time.localtime() #creating a time object
time_obj = time.gmtime() #calculates the global time 
print(time_obj)
readable_obj = time.strftime("format" , time_obj)#format is a string of diff directives like the once used below
print(readable_obj)
readable_obj = time.strftime("%H:%M %p %D %A %B ",time_obj)#https://docs.python.org/3/library/time.html
print(readable_obj)

#----------------------------------------------------------------------------------------------------------------------
time_string = "7 august, 2005"
time_new_obj = time.strptime(time_string,"%d %B, %Y")
print(time_new_obj)

#----------------------------------------------------------------------------------------------------------------------

#(year , month , day ,hours ,  minutes , secs , #day of the week , day of the year , dst(-1,0))
time_tupil = ( 2020, 8 , 7 , 12 , 0 , 0 , 4 , 0 , 0 )
time_string  = time.asctime(time_tupil) #converts the tupil to readable time
time_numbers = time.mktime(time_tupil)#converts the tupil to epoch time
print(time_string)
print(time_numbers)