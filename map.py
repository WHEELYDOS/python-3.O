#map()= applies a function to each item in a itterable (list , tuples , etc.)

#map(funtion,iterables)

store = [("pencile",25),
         ("pen",40),
         ("book",250),
         ("pancake",252)       
            ]

to_dolars = lambda store : (store[0],(store[1]/83) )

store_data = list(map(to_dolars,store))
to_rupees = lambda store_data: (store_data[0] , store_data[1]*83) 
new_data = list(map(to_rupees,store_data))
for i in store_data:
    print(i)
for i in new_data:
    print(i)

