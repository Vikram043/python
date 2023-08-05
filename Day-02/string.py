str1 = "PyNaTive"

lowercase_chars = [char for char in str1 if char.islower()]
uppercase_chars = [char for char in str1 if char.isupper()]

sorted_str = ''.join(lowercase_chars + uppercase_chars)
print(sorted_str)
