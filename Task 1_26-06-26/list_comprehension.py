#    LIST COMPREHENSIONS

squares = [ {x:x**2} for x in range(5)]
print(squares)

even_squares = [ {x:x**2 for x in range(5) if x%2==0}]
print(even_squares)

l1 = [1,2,3,4,5]
l2 = ['a','b','c','d','e']

make_dic = [ {i:j} for i , j in zip(l2,l1) ]   # zip function to map 2 lists based on their index 
print(make_dic)



