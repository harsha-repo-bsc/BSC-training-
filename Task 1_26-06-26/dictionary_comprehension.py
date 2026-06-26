dic = {'arun': 1, 'barath': 2, 'chandu': 3, 'dany': 4,'eshwar': 5}
swapped_dic = { value : key for key , value in dic.items()}

print(swapped_dic)

# create uppercase keys or values 

upper_case = { value.upper() : key for key , value in swapped_dic.items()}
print(upper_case)

# conditional dictionaries

d = { x: { 'even' if x%2==0 else 'odd'} for x in range(5) }
print(d)

