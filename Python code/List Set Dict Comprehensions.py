'''Create a Dictionary which contains the Binary values mapping with numbers found in the below integer and binary and save it in binary_dict.'''
'''    integer = [0, 1, 2, 3, 4]
    binary = ["0", "1", "10", "11", "100"]
    binary_dict = {0:"0", 1:"1", 2:"10", 3: "11", 4:"100"}'''

integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]
z = zip(integer,binary)
print(z)

for i in z:
    print(i)
binary_dict = {integer:binary for integer,binary in zip(integer,binary)} #self append binary_dict
print(binary_dict)



'''Create a List which contains additive inverse of a given integer list. An additive inverse a for an integer i is a number such that:'''
'''integer = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = [-1, 1, -2, -3, -5, 0, 7]'''

integer = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = [(0-i) for i in integer] #self append additive_inverse list
print(additive_inverse)




'''Create a set which only contains unique sqaures from a given a integer list.'''
'''integer = [1, -1, 2, -2, 3, -3]
sq_set = {1, 4, 9}'''

integer = [1, -1, 2, -2, 3, -3]
sq_set = {i*i for i in integer} # for SET use {} backet to avoid dublication.
print(sq_set)