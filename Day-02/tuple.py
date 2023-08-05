tuple1 = (11, [22, 33], 44, 55)

# Convert the tuple to a list
list_inside_tuple = list(tuple1[1])

# Modify the first item of the list
list_inside_tuple[0] = 222

# Convert the list back to a tuple
modified_tuple = (tuple1[0], tuple(list_inside_tuple), tuple1[2], tuple1[3])

print(modified_tuple)
