def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1
    x, y = y, x
    print(f'Swapped values: x = {x}, y = {y}')

# Task 2
# Invoke the function "swap" using the following scenarios:
result1 = swap("Apple", 10)  # This will return -1
result2 = swap(9, 17)        # This will print: Swapped values: x = 17, y = 9
