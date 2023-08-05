list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

concatenated_list = [list1[i] + list2[i] for i in range(min(len(list1), len(list2)))]

# Adding leftover items
concatenated_list += list1[len(list2):] + list2[len(list1):]

print(concatenated_list)
