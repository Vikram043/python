list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

concatenated_list = [x + y for x in list1 for y in list2]
print(concatenated_list)
