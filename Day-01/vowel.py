def count_vowels(input_str):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_str if char in vowels)
    return count

input_str = "Hello"
num_vowels = count_vowels(input_str)
print(f"Number of vowels: {num_vowels}")
