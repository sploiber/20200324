a = {"coronavirus": 7, 7: 24}

# Add a key
a.update({"isolation": "success"})
print(a)

# Print the values, returned as a list
print(a.values())

# Print the keys, returned as a list
print(a.keys())

# Pop a key - remove an item
a.pop(7)
