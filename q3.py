def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if key in dct:
        print(f'Original value: {dct[key]}')
    dct[key] = value
    return dct

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
result1 = update_dictionary({}, "name", "Alice")  # This will return {'name': 'Alice'}
result2 = update_dictionary({"age": 25}, "age", 26)  # This will print: Original value: 25 and return {'age': 26}
