sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]
result_dict = {key: sample_dict[key] for key in keys}
print(result_dict)
