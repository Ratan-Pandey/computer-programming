#Reverse a Dictionary
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
print("Reversed Dictionary:", reversed_dict)
